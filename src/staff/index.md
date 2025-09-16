---
title: 🙋 Staff / Office Hours
template: no-toc.html
nav_order: 103
description: A listing of all the course staff members.
extra_css: ['staff.scss']
---


## Instructor

<div class="role">
  {% for page in (staff | sort(attribute='meta.name')) if page.meta.role == 'Instructor' %}
    {% include 'staffer.html' %}
    {{ "<hr>" if not loop.last }}
  {% endfor %}
</div>

## Computing Support

<div class="role">
  {% for page in (staff | sort(attribute='meta.name')) if page.meta.role == 'Computing Support' %}
    {% include 'staffer.html' %}
    {{ "<hr>" if not loop.last }}
  {% endfor %}
</div>
