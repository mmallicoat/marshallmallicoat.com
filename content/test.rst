:title: Test Page
:date: 2018-09-17
:slug: test
:category: Meta
:status: draft

Table of Contents
-----------------

.. contents:: Table of Contents

.. meta::
    :description lang=en: An amusing story
    :description lang=fr: Une histoire amusante

References
----------

`Interpreted text roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`__

`Directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`__

Header and Footer
-----------------

.. header:: Header

.. footer:: Footer

Date and Time
-------------

.. Commented out
.. .. |date| date::
.. .. |time| date:: %H:%M
.. Today's date is |date|. This document generated at |time|.


Raw HTML
--------

.. raw:: html
    
    <p><a href="gopher://gopher.black/">raw HTML link to gopher site</a></p>

.. raw:: html
    
    <p><cite><a href="https://en.wikipedia.org/wiki/Iliad">Iliad (raw HTML)</a></cite></p>

Another line

.. role:: raw-html(raw)
    :format: html

A line a line
:raw-html:`<br/>`
broken here

:raw-html:`<cite><a href="https://en.wikipedia.org/wiki/Iliad">Iliad (raw HTML)</a></cite></p>`


Decorations
-----------

*italtics using asterisks*

:emphasis:`italitcs using directive`

:strong:`bolded with directive`

math: x\ :sup:`2`

:t:`Paradise Lost`

:title:`The Iliad`

Text Blocks
-----------

.. epigraph::

    No matter where you go, there you are.

    --Buckaroo Bonzai

.. topic:: Topic

    Aa whole lot  of text herea whole lot of  text herea whole lot
    pof text herea whole lot of text herea whole lot of text herea
    whole lot of  text herea whole lot of text  herea whole lot of
    text herea whole lot of text here whole lot of text here.

.. line-block::

    preformated text, i hope
    to be displayed here with
    linebreaks

.. container:: section
    
    This text to be in its own <section>: 
    aa whole lot  of text herea whole lot of  text herea whole lot
    pof text herea whole lot of text herea whole lot of text herea
    whole lot of  text herea whole lot of text  herea whole lot of
    text herea whole lot of text here whole lot of text here.
