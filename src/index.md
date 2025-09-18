---
title: 🏡 Home
heading: QSS 20. Modern Statistical Computing
template: no-toc.html
nav_order: 0
description: >-
  Modern Statistical Computing, Fall 2025
extra_css: ["schedule.scss"]
---

<!-- ## Announcements {: .mt-4 }
{% for announcement in (announcements | sort(attribute="meta.date", reverse=True))[:3] %}
{% if loop.first %}
{% set expand = True %}
{% endif %}
{% include 'announcement.html' %}
{% endfor %}

{% if announcements | length >= 3 %}
[All Announcements](/announcements.md){: .btn .btn-373 .fs-3}
{% endif %}


{# build up list of days #}

{% set assignment_abbr = {"project": "P", "exercise": "E"} %}


{% macro add_entries(days, group, defaults, start, counts, dummy_days=[]) %}
{% if group.default_type == "lecture" %}
    {% set dates = dates_gen_with_dummies(start, group.days, dummy_days) %}
{% else %}
    {% set dates = dates_gen(start, group.days) %}
{% endif %}

{% for day in group.entries %}

{% set type = day.type or group.default_type %}
{% set num = day.num or count(type, counts) %}
{% set date = dates.__next__() %}

{% do day.update({'type': type, 'num': num, 'date': date}) %}
{% do set_week(day, start) %}

{% do merge_in_place(day, defaults.get(type, {})) %}

{% do days.append(day) %}
{% endfor %}
{% endmacro %}

{#
operates on events, since returning ints with macros is hard
will not overwrite existing event.week
#}
{% macro set_week(event, start) %}
{% set week = (event.date - start).days // 7 + 1 %}
{% do event.setdefault('week', week) %}
{% endmacro %}


{% macro add_assignments(assignments, group, defaults, counts) %}
{% for assignment in group.entries %}


{% set type = assignment.type or group.default_type %}
{% set num = assignment.num or count(type, counts) %}

{% do assignment.update({'type': type, 'num': num, 'start': parse_date(assignment.start), 'end': parse_date(assignment.end)}) %}
{% do merge_in_place(assignment, defaults.get(type, {})) %}

{% if not assignment.hide_in_cal %}
{% do add_assignment(assignment, assignments, 'start', start) %}
{% do add_assignment(assignment, assignments, 'end', start) %}
{% endif %}
{% endfor %}
{% endmacro %}


{% macro add_assignment(assignment, assignments, type, start) %}
{% set event = {'assignment': assignment, 'type': type, 'date': assignment[type]} %}
{% do set_week(event, start) %}
{% do assignments.append(event) %}
{% do assignment.setdefault(type~"_event", event) %}
{% endmacro %}

{#
merge d2 into d1, in place
dicts are merged recursively; other existing values are not changed
#}
{% macro merge_in_place(d1, d2) %}
{% for k, v in d2.items() %}
{% set existing_val = d1.setdefault(k, v) %}
{% if existing_val != v and existing_val is mapping and v is mapping %}
{% do d1.__setitem__(k, merge_dicts(existing_val, v)) %}
{% endif %}
{% endfor %}
{% endmacro %}

{%- macro count(type, counts) %}
{%- set c = counts[type] %}
{%- if c is undefined %}
{{- -1 }}
{%- else %}
{%- do counts.__setitem__(type, c + 1) %}
{{- c + 1 }}
{%- endif %}
{%- endmacro %}

{% set counts = {} %}
{% if schedule.start_indices %}
{% for type, index in schedule.start_indices.items() %}
{% do counts.__setitem__(type, index - 1) %}
{% endfor %}
{% endif %}

{% set days = [] %}
{% set assignment_dates = [] %}

{% set start = parse_date(schedule.start) %}
{# add lectures #}
{% do add_entries(days, schedule.lectures, schedule.defaults, start, counts, schedule.dummy_days) %}
{% set days = days|sort(attribute="date") %}
{# add assignments #}
{% do add_assignments(assignment_dates, schedule.projects, schedule.defaults, counts) %}
{% do add_assignments(assignment_dates, schedule.exercises, schedule.defaults, counts) %}
{# sort by date; latest to earliest (ties broken by end-date before start-date #}
{% set assignment_dates = assignment_dates|sort(attribute='date,type', reverse=true) %}


{% macro update_assignment_status(events, day, active, status) %}

{% if events %}
{% if events[-1].date <= day.date %}
{% set event = events.pop() %}

{% if event.assignment.type == "project" %}

{% if event.type == "start" %}
{% set active.project = event.assignment %}
{% elif event.type == "end" %}
{% set active.project = none %}
{% endif %}

{% do status.project.append(event.type) %}

{% elif event.assignment.type == "exercise" %}

{% if event.type == "start" %}
{% set active.exercise = event.assignment %}
{% elif event.type == "end" %}
{% set active.exercise = none %}
{% endif %}

{% do status.exercise.append(event.type) %}

{% endif %}

{% do update_assignment_status(events, day, active, status) %}
{% else %}

{% if status.project|length == 0 %}
{% do status.project.append("active" if active.project is not none else "inactive") %}
{% endif %}
{% if status.exercise|length == 0 %}
{% do status.exercise.append("active" if active.exercise is not none else "inactive") %}
{% endif %}
{% endif %}
{% endif %}

{% endmacro %}


{% macro increment_lengths(items, amount=1) %}
{% for type in ["exercise", "project"] %}
{% set item = items[type] %}
{% if item %}
{% do item.__setitem__('length', item.get('length', 0) + amount) %}
{% endif %}
{% endfor %}
{% endmacro %}


{%- macro classes() %}
{{- varargs[-1] }}
{%- for c in deep_get(schedule.styles, *varargs, default=[]) %} {{ c }}{% endfor %}
{%- endmacro %}


{# first pass to calculate assignment lengths #}
{% set active_assignments = namespace(project=none, exercise=none) %}
{% set assignment_dates_copy = assignment_dates[:] %}
{% for day in days %}
{% if loop.changed(day.week) %}
{% do increment_lengths(active_assignments) %}
{% endif %}
{% set status = namespace(project=[], exercise=[]) %}
{% do increment_lengths(active_assignments) %}
{% do update_assignment_status(assignment_dates_copy, day, active_assignments, status) %}
{% do increment_lengths(active_assignments) %}
{% endfor %} -->

<!-- !!! info
    Welcome to POLI 179: Special Topics in Political Methodology -- Applied Deep Representation Learning for Social Science. The first class meeting is on Tuesday, April 2nd 6:30–7:50 PM at [Franklin Antonio Hall 1450](https://maps.app.goo.gl/1D9FsWWfe1bGzptE9). -->

<!-- QSS 20 is a foundational and required course in the Quantitative Social Science curriculum that equips students with the computing literacy to conduct social science research in the age of “big data.” The skills students learn in QSS 20 are building blocks for data science applications from research to industry to nonprofits and government. -->

<!-- ## Calendar {: .mt-5 } -->

<!-- Below is a rough sketch of the quarter and things are subject to change. -->

{# second pass to output table #}
{% set active_assignments = namespace(project=none, exercise=none) %}
<table class="table course-calendar">
<thead>
<tr class="calendar-start">
    <th></th>
    <th>Topic</th>
    <th class="dummy"></th>
    <th>Homeworks</th>
    <th>Project</th>
</tr>
</thead>
<tbody>
{% for day in days %}

{# update assignment status #}
{% set status = namespace(project=[], exercise=[]) %}
{% do update_assignment_status(assignment_dates, day, active_assignments, status) %}

{%- if loop.changed(day.week) %}
<tr class="week-start">
<td colspan="2" class="week-name">Week {{ day.week }}
    <!-- {% if  schedule.weeks[day.week] %} - {{ schedule.weeks[day.week]}} {% endif %} -->
    </td>
<td class="dummy"></td>
{% for type in ["exercise", "project"] %}
{% if "active" not in status[type] and "end" not in status[type] %}
<td class="{{ type }}-inactive"></td>
{% endif %}
{% endfor %}
</tr>
{%- endif %}
<tr class="row-{{ day.type }}">
<td rowspan="2" class="class-date">{{ day.date.strftime("%a %-m/%-d") }}</td>
{% if day.is_dummy %}
<td rowspan="2" class="class-data">
    {% if day.show_title %}
        <span class="class-title-text">{{ day.title }}</span>
    {% endif %}
</td>
{% else %}
<td rowspan="2" class="class-data">
<div class="class-title">
    <!-- {%- if day.is_exam %}
    <span class="class-title-label label-373 label-exam">EXAM OH</span>
    {%- elif day.type == "lecture" %}
    <span class="class-title-label label-373 label-lecture">LEC {{ "{:>02}".format(day.num) }}</span>
    {%- elif day.type == "section" %}
    <span class="class-title-label label-373 label-section">SEC {{ "{:>02}".format(day.num)  }}</span>
    {%- elif day.type == "holiday" %}
    <span class="class-title-label label-373 label-holiday">HOLIDAY</span>
    {%- endif %} -->

    <span class="class-title-text">{{ day.title }}</span>
</div>
{% set resources = day.get('resources', {}).items()|selectattr(1) %}
{% if resources %}
{% set lessonsExpandName = "lesson-"~day.date.strftime("%m-%d") %}
<div class="class-resources">
{% for res_type, res in resources %}
<div class="resource-group resource-group-{{ res_type }}">
<span class="resource-label">{{ res_type }}:</span>
<span class="{{ classes('resources', res_type, 'resource-links') }}">
{% for res_name, res_url in res.items() %}
{% set display_res_name = res_name | replace("_", " ") %}
{%- if res_name == 'videos' and res_url %}
<a href="#{{ lessonsExpandName }}-video" data-toggle="collapse" class="{{ classes('resources', res_type, 'resource-link') }} {{ res_name }} collapsed">{{ display_res_name }}</a>
{%- elif res_name == 'files' and res_url %}
<a href="#{{ lessonsExpandName }}-files" data-toggle="collapse" class="{{ classes('resources', res_type, 'resource-link') }} {{ res_name }} collapsed">{{ display_res_name }}</a>
{%- elif res_url %}
<a href="{{ res_url.format(**day)|url }}" class="{{ classes('resources', res_type, 'resource-link') }} {{ res_name }}">{{ display_res_name }}</a>
{%- else %}
<a class="{{ classes('resources', res_type, 'resource-link') }} {{ res_name }} disabled">{{ display_res_name }}</a>
{%- endif %}
{%- if not loop.last and res_type not in ['lesson', 'worksheet', 'lecture', 'resources', 'Optional Resources'] %}, {% endif %}
{% endfor %}
</span>
</div>
{% if 'videos' in res %}
<div class="collapse lesson-videos" id="{{ lessonsExpandName }}-video">
  <div class="card card-body">
    {% for video in res['videos'] %}
        <span>
            <a class="itempool-link" href="{{ video.url }}">{{ video.name }}</a>
        </span>
    {% endfor %}
  </div>
</div>
{% endif %}
{% if 'files' in res %}
<div class="collapse lesson-files" id="{{ lessonsExpandName }}-files">
  <div class="card card-body">
    <span>All files available in one <a href="{{res['files'].format(**day) | url}}">zip</a>.</span>
    <br />
    <p>
        <em>To download all files at once, type the following commands in a shell on your machine:</em>
    </p>
    ```
    wget {{res['files'].format(**day) | url}}
    unzip lecture{{day.num}}.zip
    ```
  </div>
</div>
{% endif %}
{% endfor %}
</div>
{% endif %}
</td>
{% endif %}


<td class="dummy"></td>
{% for type in ["exercise", "project"] %}
{% if "active" not in status[type] and "end" not in status[type] %}
<td class="{{ type }}-inactive"></td>
{% endif %}
{% endfor %}
</tr>

<tr class="row-{{ day.type }}">
<td class="dummy"></td>
{% for type in ["exercise", "project"] %}
{% if "start" in status[type] %}
{% set assignment = active_assignments[type] %}
{% set real_type = 'exam' if (assignment.is_exam) else assignment.type %}
<td rowspan="{{ assignment.length }}" class="assignment {{ real_type }} {{ 'active' if assignment.url }}">
    <span class="assignment-boundary assignment-released">Release</span>
    {% if assignment.url %}
    <a href="{{ assignment.url.format(**assignment)|url }}" class="assignment-link stretched-link">
    {% else %}
    <a class="assignment-link stretched-link disabled">
    {% endif %}
    <div class="assignment-text">
        {%- if real_type == "exercise" %}
            <span class="assignment-label label-373 label-exercise">HW{{ assignment.num }}</span>
            <div class="assignment-title">{{ assignment.title }}</div>
        {%- elif real_type == "project" %}
            <!-- <span class="assignment-label label-373 label-project">R{{ assignment.num }}</span> -->
            <div class="assignment-title">{{ assignment.title }}</div>
        {%- elif real_type == "exam" %}
            <span class="assignment-label label-373 label-exam">EXAM {{ '' if assignment.hide_num else assignment.num}}</span>
            <div class="assignment-title">{{ assignment.title }}</div>
        {%- endif %}
    </div>
    </a>
    <span class="assignment-boundary assignment-due">Due {{ assignment.due }}</span>
</td>
{% elif "active" not in status[type] %}
<td class="{{ type }}-inactive"></td>
{% endif %}
{% endfor %}
</tr>
{% endfor %}
</tbody>
</table>
