:title: HTML Notes
:date: 2017-11-12
:modified: 2017-11-12
:category: Meta
:slug: html-notes

Global Attributes
~~~~~~~~~~~~~~~~~
* These are attributes that can be applied to any element.
* They include:

  * ``class``: Value will be a set of space-separated tokens
    represented all of the classes to which the element
    belongs. Little restriction on values, but should be
    used to "describe the nature of the content" rather than
    to describe the "*desired presentation* of the content".
    Classes can be used with CSS selectors for styling.
  * ``lang``: Specifies language of element contents.
  * ``translate``: Used to indicate if something should be
    translated when the page is localized.
  * ``id``: Gives an element a unique identifier.
  * ``style``: For CSS styling.
  * ``title``: Advisory info on an element, such as "would be
    appropriate for a tooltip". For a link, this would be a
    title or description of the target resource. For a
    citation, it would be further info about the source.
    This attribute is **discouraged** since the value may
    not be accessible to people on phones/tablets.

html Element
~~~~~~~~~~~~
* Root of document. Contains ``head`` and ``body``.
* Should have the ``lang`` attribute set (e.g. ``en``).

head Element
~~~~~~~~~~~~

* Contains metadata content: content that sets the
  "presentation or behavior of the rest of the content" or
  that sets up the "relationship of the document with other
  documents".

* Metadata elements include:

  * ``title``: Advisory info; see above.

  * ``script``: JavaScript, etc.

  * ``style``: CSS

  * ``link``: Links document to other resources. Must have
    a ``rel`` attribute. Used to link a stylesheet, for
    example.

  * ``meta``: Represents metadata that cannot be expressed
    using ``title``, ``base``, ``link``, ``style``, or
    ``script``. Contains attributes ``name``, ``charset``
    (which is used to set UTF-8), and others.

body Element and Sections
~~~~~~~~~~~~~~~~~~~~~~~~~
* _`Sectioning content` defines the scope of headings and
  footers. These elements include: ``article``, ``aside``,
  ``nav``, and ``section``.
* _`Sectioning root`: ``blockquote``, ``body``, ``fieldset``,
  ``figure``, ``td``. Used for outlines (?).

* ``body`` contains the content of the document.

* ``article``: "When the main content of the page (i.e. excluding footers,
  headers, navigation blocks, and sidebars)
  is all one single self-contained composition, the content
  should be marked up with a ``main`` element and the content
  may also be marked with an ``article``, but it is
  **technically redundant** in this case (since it's
  self-evident that the page is a single composition, as it
  is a single document)."

  It can contain a ``header`` and/or ``footer``.

* ``section``: Generic section of a document, i.e. a
  thematic grouping of the content. The theme should be
  identified by including a heading. ``article`` should be
  used instead when it would make sense to syndicate the
  contents of the element.

* ``article`` vs. ``section``: "A ``section`` forms part of
  something else. An ``article`` is its own thing. But how
  does one know which is which? Mostly the real answer is 'it
  depends on author intent'." 

* ``nav``: Section of a page that links to other pages or 
  parts within the page, such as navigation links. 

  "In particular, it is common for footers to have a short
  list of links to various pages of a site, such as the terms
  of service, the home page, and a copyright page. The
  ``footer`` element **alone is sufficient** for such cases;
  while a ``nav`` element can be used in such cases, it is
  usually unnecessary."

  Links within the ``nav`` sometimes put into a unordered
  list.

* ``aside``: Used for tangentially related content. Often
  represented as sidebars. Used for pull quotes. **Not**
  appropriate for parentheticals within the main document.

* headings (``h1``, ``h2``, etc.): Used to head sections.

* ``header``: Introductory content for a section. Often
  contains a heading.

* ``footer``: Contains information on authors, links to
  related documents, copyright data, etc. Can also be used
  for appendices, indices, long colophons. They don't
  necessarily have to appear at the *end* of a section.

  Contact info
  should be inside an ``address`` element, possibly within
  a ``header`` or ``footer``.

* ``address``: Gives contact information. Often within a
  ``footer`` element.

* An _`outline` for a `sectioning content`_ element or a
  `sectioning root`_ element consists of a list of one or
  more nested *sections*. "A **section** is a container that
  corresponds to some nodes in the original DOM tree. Each
  section can have one heading associated with it, and can
  contain any number of further nested sections."


Grouping content
~~~~~~~~~~~~~~~~
* ``p``, ``blockquote``, ``ol``, etc.
* ``dl``, ``dd``, ``dt``: association lists (?)
* ``main``: Represents main content of the ``body`` of a
  document. It is **not** `sectioning content`_ and has no
  effect on the document *outline*.
  
  ``main`` should not be a descendent of:
  ``article``, ``aside``, ``footer``, ``header``, or ``nav``.
* ``div``: Generic container?

Text-level semantics
~~~~~~~~~~~~~~~~~~~~
* ``em`` (emphasis)
* ``strong`` (bold)
* ``cite`` (citations)
* ``q`` (quotes)
* ``abbr`` (abbreviation)
* ``time``
* ``code``
* ``i``: Text in an alternate voice or mood, such as a
  technical term or idiomatic phrase from another language.
* ``b``: Text to which attention is being drawn for
  utilitarian purposes, without any extra importance
  or an alternate voice or mood.
* ``u``: Text with an unarticulate, though explicitly
  rendered, non-textual annotation. (?)
* ``span``: Has no explicit meaning. Used with ``class``,
  ``lang``, or ``dir`` attributes.


