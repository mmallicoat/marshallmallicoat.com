---
layout: default
title: Archive
---
<div class="archive">
	<h1>Archive</h1>
	<ul>
	    {% for post in site.posts %}
			<li>
				<span>
					{{post.date | date: "%-d %b %Y"}} &nbsp;
				</span> 
				&raquo;
				<a href="{{ post.url }}">{{post.title}}</a>
			</li>
    	{% endfor %}
   	</ul>
</div>

<footer>
	<p class="nav">
		<span class="left">
			<a href="/contact.html">Contact</a>
		</span>
		<span class="right">
			<a href="/feed.xml">Feed</a>
		</span>
	</p>
</footer>
