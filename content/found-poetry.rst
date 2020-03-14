:title:  Found Poetry
:date:   2020-03-13
:slug: found-poetry


While reading a news article [#article]_ with the w3m_ text-based Web browser,
I noticed strange sentences interspersed in the typical markup gore you see
when reading Web pages without JavaScript enabled.

::

    The UK government warns Trump that war with Iran 'is in none of our interests'
    
    Adam Bienkov
    2020-01-03T10:33:25Z
     The letter F.  An envelope. It indicates the ability to send an email.  An
    image of a chain link. It symobilizes a website link url.  A stylized bird
    with an open mouth, tweeting.  The word "in".  A stylized letter F.
     Three evenly spaced dots forming an ellipsis: "...". Two crossed lines that
    form an 'X'. It indicates a way to close an interaction, or dismiss a
    notification.
    Donald Trump Boris Johnson Donald Trump Boris Johnson [5e0f163885]
    Donald Trump and Boris Johnson. Getty
    
      • The UK on Friday warned US President Donald Trump against outright war
        with Iran.
      • The foreign secretary, Dominic Raab, said that further conflict "is in
        none of our interests."
      • Iran and the US are on the brink of war after Trump ordered an airstrike
        that killed Iranian Maj. Gen. Qassem Soleimani late Thursday.
      • An adviser to Iranian President Hassan Rouhani said the US had crossed a
        "red line," and the country&apos;s supreme leader, Ayatollah Ali Khamenei,
        warned of "harsh retaliation."
    
    The UK government on Friday urged President Donald Trump to step back from
    outright war with Iran after a US airstrike killed Iran&apos;s elite Quds
    Force commander, Maj. Gen. Qassem Soleimani, warning that further conflict in
    the region "is in none of our interests."

The parts that stuck out to me were:

*   The letter F.
*   An envelope. It indicates the ability to send an email.
*   An image of a chain link. It symobilizes a website link url.
*   A stylized bird with an open mouth, tweeting.

And so forth. What are these anyway? The Web page has a bunch of icons which
are also hyperlinks. The icon class contains a non-standard HTML element
``<desc>`` which contains a description of the icon (perhaps in a gesture of
accessibility toward people with vision impairment). The block looks something
like:

.. code:: html

    <a href="https://www.facebook.com">
        <svg class="svg-icon facebook-icon">
            <title id="title">Facebook Icon</title>
            <desc id="desc">The letter F.</desc>
        </svg>
    </a>
 
The body of the ``<desc>`` elements get dumped into the visible text in the w3m
browser. Read together, they are quite moving—almost liberatory. Here are these
little snippets, with all of article and other junk stripped out.



.. _w3m: https://en.wikipedia.org/wiki/W3m

.. [#article] Bienkov, Adam. "The UK government warns Trump that war with Iran 'is in none of our interests'."
    *Business Insider*, 2 Jan. 2020,
    `<https://www.businessinsider.com/uk-warns-donald-trump-against-launching-war-iran-qassem-soleimani-2020-1>`__.
    Accessed 13 March 2020. 
