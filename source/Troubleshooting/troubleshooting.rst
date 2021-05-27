.. _TroubleshootingDoc:

Troubleshooting
==================

.. _DiagnosingInfeasibleRunsSection:

Basic Troubleshooting
--------------------------
In the event of an application-breaking bug, the user should reload the page - it may
have been a temporary bug. A second step (if needed) is to do a cleared-cache reload
of the page (Ctrl+F5 in browsers on Windows. Shift+Cmd+R in Firefox/Chrome on Mac -
see here for more options, including Safari). Clearing the cache and reloading helps
particularly if a new version of the application has been deployed, but the browser is still
holding onto part of the old version - the application attempts to clear out older versions,
but occasionally there could be bugs.

If those do not work, the user should try closing the tab and reopening the application
from the home page, as opposed to the page the user was initially on. If a model run
has some kind of bad data associated with it, for example, then loading that model run
may fail even if the rest of the application works correctly.
Finally, get in touch with the development team by emailing nsantos5@ucmerced.edu if
other significant bugs are found, as these reports will help the development team to
avoid those in the future. The development team maintains logging information in the
application that should capture most errors, but the including the following information in
emails will help in diagnosing the problem:

1. The action taken in the application
2. The expected result of the action
3. The actual result
4. The full page URL
5. And if possible the approximate time the action was attempted (this will facilitate
looking for any data in the logging system - it only logs errors inside the
application and not anything else)


Diagnosing infeasible model runs
----------------------------------