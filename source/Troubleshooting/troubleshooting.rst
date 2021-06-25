.. _TroubleshootingDoc:

Troubleshooting
==================

.. _DiagnosingInfeasibleRunsSection:

Basic Troubleshooting
--------------------------
In the event of an application-breaking bug, reload the page - it may
have been a temporary bug. A second step (if needed) is a cleared-cache reload
of the page (Ctrl+F5 in browsers on Windows. Shift+Cmd+R in Firefox/Chrome on Mac -
`see here for more options <https://www.howtogeek.com/672607/how-to-hard-refresh-your-web-browser-to-bypass-your-cache/>`_,
including Safari). Clearing the cache and reloading helps
particularly if a new version of the application has been deployed, but the browser is still
holding onto part of the old version - the application attempts to clear out older versions,
but occasionally there could be bugs.

If those do not work, try closing the tab and reopening the application
from the home page, as opposed to the page the user was initially on. If a model run
has some kind of bad data associated with it, for example, then loading that model run
may fail even if the rest of the application works correctly.

Finally, if you encounter bugs or have other questions, please
`reach out on GitHub to file an issue <https://github.com/Water-Systems-Management-UCM/Waterspout/issues>`_. If you would
like to ask a question about the application, you can `start a discussion on GitHub  <https://github.com/ucm-openag/OpenAg_Docs/discussions/categories/ideas>`_ as well.
If you need to `get in touch with the development team otherwise, please use this form <https://wsm.ucmerced.edu/contact-us/>`_.

Bug reports will help the development team to identify, fix, and avoid issues in the future.
The development team maintains logging information in the
application that should capture most errors, but the including the following information in
issues filed on GitHub or via email will help in diagnosing the problem:

1. The action taken in the application
2. The expected result of the action
3. The actual result
4. The full page URL
5. And if possible the approximate time the action was attempted (this will facilitate
    looking for any data in the logging system - it only logs errors inside the
    application and not anything else)


Diagnosing infeasible model runs
----------------------------------