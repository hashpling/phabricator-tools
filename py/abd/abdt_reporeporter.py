"""Report the state of a repository."""
# =============================================================================
# CONTENTS
# -----------------------------------------------------------------------------
# abdt_reporeporter
#
# Public Classes:
#   RepoReporter
#    .on_tryloop_exception
#    .on_exception
#    .on_completed
#    .start_branch
#    .finish_branch
#    .close
#
# -----------------------------------------------------------------------------
# (this contents block is generated, edits will be lost)
# =============================================================================

import phlsys_subprocess


class RepoReporter(object):

    def __init__(self, try_filename, ok_filename):
        """Initialise a new reporter to report to the specified files.

        :try_filename: string path to the file to touch when trying the repo
        :ok_filename: string path to the file to touch when processed the repo

        """
        super(RepoReporter, self).__init__()
        self._try_filename = try_filename
        self._ok_filename = ok_filename
        phlsys_subprocess.run("touch", self._try_filename)

    def on_tryloop_exception(self, e, delay):
        self._repo_report(str(e) + "\nwill wait " + str(delay))

    def on_exception(self, e):
        self._repo_report(str(e))

    def on_completed(self):
        phlsys_subprocess.run("touch", self._ok_filename)

    def start_branch(self, branch):
        _ = branch  # NOQA
        self._repo_report('start branch')

    def finish_branch(self, branch):
        _ = branch  # NOQA
        self._repo_report('finish branch')

    def _repo_report(self, s):
        pass

    def close(self):
        """Close any resources associated with the report."""
        pass


#------------------------------------------------------------------------------
# Copyright (C) 2012 Bloomberg L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#------------------------------- END-OF-FILE ----------------------------------
