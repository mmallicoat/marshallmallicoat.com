:title: Blog Redesign
:date: 2017-10-22
:modified: 2017-11-09
:category: Meta
:slug: todo
:status: draft

Todo
----
* Use ALA state abbreviations in Readings? What is NY?
* Need a directive to indicate emphasis in a semantic way?
* How to indicate citation of other works, like book in footnote? Or Twilight movie?
  There exists an HTML tag ``<cite>`` which is maybe the one to use.
  How to code this in RST?
* Need to go back through essays and clean up the markup
* In ``base.html`` template, add metadata like author to head?
* In ``about.html`` page, use ``address`` element,
  maybe in the vCard (?) microformat.
* Add a favicon?
* Do I really need a sitemap? Some `tips <https://github.com/getpelican/pelican/wiki/Tips-n-Tricks>`_ to implement this.

Git
---
* I have created a local branch called ``pelican`` of the git repo.
* When I push to the master branch, I need to do it correctly.
  This `Stackoverflow question <https://stackoverflow.com/questions/4752387/pushing-a-local-branch-up-to-github>`_ has some info that might
  be helpful.

Design Notes
------------
* Maybe redesign the view, e.g. maybe a white background. `This site`_ has nice text.
* `Tufte CSS`_ provides CSS guidance/stylesheets based on typography theory.
  I may be able to rely on this heavily.

.. _`This site`: https://hamberg.no/erlend/
.. _`Tufte CSS`: https://edwardtufte.github.io/tufte-css/


Other Thoughts
--------------
* I think we want a single directory for all non-personal notes, both drafts and final. The draft status can be set with a meta tag, which Pelican can use to decide to include or not.
* We will keep a last modified date for each document.
* I think in Pelican you can have a "drafts" category which can be set to not be published.

Done
----
* Maybe add a symbol on the title banner by *HEAP*, e.g. a triangle (like a pile of
  sand in an hourglass). This would be like Winston's "Five-Star" method, i.e.
  adding a *symbol*.
* Get HTML structure to match previous blog.
* On second thought, maybe should strip the HTML down: remove all unnecessary
  classes and ids. Focus on the *structure*, guiding by the HTML specification.
  Try to make the tree structure clear and correct.
  Don't worry about the presentation at all for now. Just use the Tufte CSS unaltered.
* How to do em-dashes in rST? Can't. Have to use ``^V`` thing in vim.
