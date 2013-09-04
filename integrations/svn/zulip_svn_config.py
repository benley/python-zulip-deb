#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2013 Zulip, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Change these values to configure authentication for the plugin
ZULIP_USER = "svn-bot@example.com"
ZULIP_API_KEY = "0123456789abcdef0123456789abcdef"

# commit_notice_destination() lets you customize where commit notices
# are sent to with the full power of a Python function.
#
# It takes the following arguments:
# * path   = the path to the svn repository on the server
# * commit = the commit id
#
# Returns a dictionary encoding the stream and subject to send the
# notification to (or None to send no notification).
#
# The default code below will send every commit except for the "master-plan"
# and "secret" repos to
# * stream "commits"
# * subject "deploy => branch_name" (using a pretty unicode right arrow)
def commit_notice_destination(path, commit):
    repo = path.split('/')[-1]
    if repo not in ["evil-master-plan", "my-super-secret-repository"]:
        return dict(stream  = "commits",
                    subject = u"deploy \u21D2 %s" % (repo,))

    # Return None for cases where you don't want a notice sent
    return None

## If properly installed, the Zulip API should be in your import
## path, but if not, set a custom path below
ZULIP_API_PATH = None

# This should not need to change unless you have a custom Zulip subdomain.
ZULIP_SITE = "https://api.zulip.com"
