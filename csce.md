---
layout: default
title: CSCE Schedule
---
# CSCE Schedule

<!-- posts and pages used as sources -->
{% assign all = null | compact %}
{% assign all = all | concat:site.posts | concat:site.pages %}

<!-- Setup order for Units -->
{% assign units = "1,2,3,4,5,6" | split: ',' %}
{% for unit in units %}

  <!-- Each Unit has a range of weeks and a heading -->
  {% if unit == "1" %} 
      {% assign start = 0 %}
      {% assign end = 3 %}
## Unit {{unit}}: Introduction to Tools and Resources
> The initial weeks focus on introducing Tools, Pair Programming, and tools we will using throughout the year. At the end of Weeks 0-3, students will be blogging on GitHub and creating GitHub Pages; introduced to Jupyter Notebooks and VSCode, coding with JavaScript, HTML, and CSS

  {% elsif unit == "2" %} 
      {% assign start = 4 %}
      {% assign end = 7 %}
## Unit {{unit}}: Introduction to Web Development
> A key focus of this course is to make Web games using JavaScript. These next few weeks we will perform the aspects of constructing a simple game and deploying the game to a simple Website.  GitHub pages got us started on these building a Website.   By by the end of this Unit, students will be ready to start many of the technical coding aspects of Web and Game Development, having established a Deployed Website.  In Nov our goal is to participate in N@tM with the Electives Department, we want you to have a couple of games to share and be able to describe how you created them using JavaScript. 

  {% elsif unit == "3" %} 
      {% assign start = 8 %}
      {% assign end = 12 %}
## Unit {{unit}}: N@tM Project, Web, Game(s), Local Storage, and Blogging.
>  This will be a time of preparing project and enhancing technical acumen.  Part of the process of becoming technically proficient is taking small and challenging steps in coding, this will often make the student uncomforatable.   But with some vision and research it is amazing what can be learned and accomplished.

{% elsif unit == "4" %} 
      {% assign start = 13 %}
      {% assign end = 16 %}
## Unit {{unit}}: Understanding internals of GitHub Pages
> Trimester 1 begins with ...
      
  {% elsif unit == "5" %} 
      {% assign start = 17 %}
      {% assign end = 20 %}
## Unit {{unit}}: 
> Trimester 2 continues with ...

{% elsif unit == "6" %} 
      {% assign start = 21 %}
      {% assign end = 24 %}
## Unit {{unit}}: Data and Algorithmic Programming
> Trimester 2 concludes with ...

  {% endif %}

  <!-- Column Headings for Blogs -->
  <table>
      <tr>
        <th>Week</th>
        <th>Sprint</th>
        <th>Code, Code, Code</th>
        <th>Tools and DevOps</th>
        <th>Human Skills</th>
      </tr>

  <!-- These loops group blogs according to Type and Week -->
  {% assign units = null | compact %}  <!-- empty array -->
  {% assign sym = "|||" %}  <!-- string/symbol used a separator  -->
  {% assign deli = sym | compact %} <!-- force to array element -->

  {% for i in (start..end) -%}
    {% assign pt = null | compact %} <!-- empty array -->
    {% assign ap = null | compact %}
    {% assign tt = null | compact %}
    {% assign hm = null | compact %}
    {% assign uk = null | compact %}

  <!-- looping through all posts -->
    {% for post in all %}

  <!-- prepare data blog post data for evaluation -->
      {% assign week = post.week | plus: 0 %}  <!-- force to integer -->
      {% assign title = post.title | compact %}
      {% assign url = post.url | compact %}

  <!-- process posts for current week -->
      {% if week == i %} 

  <!-- organizing blogs by type -->
        {% if post.type == "plan" %} 
            {% assign pt = pt | push: title %}
            {% assign pt = pt | push: url %}
        {% elsif post.type == "ap" %}
            {% assign ap = ap | push: title %}
            {% assign ap = ap | push: url %}  
        {% elsif post.type == "pbl" %}
            {% assign tt = tt | push: title %}
            {% assign tt = tt | push: url %} 
        {% elsif post.type == "human" %}
            {% assign hm = hm | push: title %}
            {% assign hm = hm | push: url %} 
        {% else %}
            {% assign uk = uk | push: title %}
            {% assign uk = uk | push: url %}     
        {% endif %}

      {% endif %}
    {% endfor %}

  <!-- ordering blogs and inserting column delimiters -->
  {% assign units = units | concat:pt | concat:deli | concat:ap | concat:deli | concat:tt | concat:deli | concat:hm %}

  <!-- Display documents by type-->
  <tr>
  <td> {{i}} </td> 
  <td>
  {% for i in (0..100) -%}   <!-- forever loop -->
    {% if units.size == 0 %} <!-- break loop when data is empty -->
      {% break %}
    {% elsif units[0] == sym %} <!-- make new column -->
      </td>
      <td>
      {% assign units = units | shift %} <!-- remove delimiter -->
    {% else %} <!-- make a link in the column -->
      - <a href="{{site.baseurl}}/{{units[1]}}">{{units[0]}}</a> <br/> 
      {% assign units = units | shift | shift %} <!-- remove title and url -->
    {% endif %}
  {% endfor %}
  </td>
  </tr>
  {% endfor %}

  </table>
{% endfor %}
