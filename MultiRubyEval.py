import sublime, sublime_plugin
from subprocess import Popen, PIPE
from collections import namedtuple

Result = namedtuple('Result', ['returncode', 'stdout', 'stderr'])

ruby_script = u"""
def get_binding(x) binding end
memo_eval = Hash.new {{ |h, k| h[k] = eval "{expr}", get_binding(k) }}
{inputs}.each {{ |x| puts memo_eval[x] }}
"""

class MultiRubyEvalCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Enter expression", "", self.done, None, None)

    def done(self, expr):
        view = self.window.active_view()
        view.run_command("multi_ruby_eval_replace_sel", { "expr": expr })

class MultiRubyEvalReplaceSel(sublime_plugin.TextCommand):
    def run(self, edit, expr=''):
        sel = self.get_selections()
        sel_str = ['"'+escape_quotes(self.view.substr(s))+'"' for s in sel]
        sel_str = '['+', '.join(sel_str)+']'
        expr = escape_quotes(expr)

        res = eval_ruby(expr, sel_str)
        if res.returncode == 0:
            self.replace_selections(edit, reversed(sel), reversed(res.stdout.split('\n')))
        else:
            self.display_error(res.stderr)

    def get_selections(self):
        sel = self.view.sel()
        if sel[0].empty():
            sel = [self.view.word(sel[0])]
        return sel

    def replace_selections(self, edit, sel, results):
        for s, line in zip(sel, results):
            self.view.replace(edit, s, line)

    def display_error(self, err):
        panel = self.view.window().get_output_panel("stderr")
        panel.run_command("insert", { "characters": err })
        self.view.window().run_command("show_panel", { "panel": "output.stderr" })

def eval_ruby(expr, inputs):
    cmd = get_ruby() + ["-e", ruby_script.format(inputs=inputs, expr=expr)]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return Result(
        returncode=p.returncode,
        stdout=out.decode('utf-8').strip(),
        stderr=err.decode('utf-8').strip()
    )

def get_ruby():
    return ["ruby"]

def escape_quotes(s):
    return s.replace('"', '\\"').replace("'", "\\'")
