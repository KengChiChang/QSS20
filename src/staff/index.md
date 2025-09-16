---
title: 🙋 Staff / Office Hours
template: no-toc.html
# nav_order: 98
description: A listing of all the course staff members.
extra_css: ['staff.scss']
---

If you have a general question that other students could potentially benefit from, please post it on Ed. For logistical questions, we ask that you post privately on Ed so the whole staff can respond.

## Instructor

<div class="role">
  {% for page in (staff | sort(attribute='meta.name')) if page.meta.role == 'Instructor' %}
    {% include 'staffer.html' %}
    {{ "<hr>" if not loop.last }}
  {% endfor %}
</div>

## Teaching Assistant

<div class="role">
  {% for page in (staff | sort(attribute='meta.name')) if page.meta.role == 'Teaching Assistant' %}
    {% include 'staffer.html' %}
    {{ "<hr>" if not loop.last }}
  {% endfor %}
</div>
