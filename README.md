# CSE 391 Website

This repo contains the course website for CSE 391. Content for this website is almost entirely written in Markdown, and a Gitlab CI runner automatically deploys the contents of this repo to the web. The template was designed specifically for 373, although there are some portions of the infrastructure that could be cleaned up.

## Development Setup

### Python Environment

We recommend using a [virtual environment](https://docs.python.org/3/library/venv.html). On Python 3.12+, create a `venv`:

```sh
python3 -m venv .venv             # create the venv
source .venv/bin/activate         # activate venv
pip3 install -r requirements.txt  # install packages w/ pip
```

Then, every time, just activate the venv!

```sh
source .venv/bin/activate.fish
```

This is particularly helpful if you need to juggle different instances of the course website.

### Local Development

In your `venv`, you should be able to run:

```sh
python3 -m mkdocs serve
```

Which should spin up a live server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

In contrast, when the site gets built, the CD will run:

```sh
python3 -m mkdocs gh-deploy --clean
```

(which converts some types of warnings to errors)

## Common Edits

You may also want to see [Notable Files for Modifying this Template](#notable-files-for-modifying-this-template).

### Changing the Schedule (Calendar, Lectures, Assignments)

All files controlling the schedule can be found in `/data/schedule/`. A detailed setup guide for the schedule at the beginning of the quarter can be found in `/data/schedule/README.md`.

### Updating Staff

The staff (i.e. instructors and TAs) are individual markdown files in `collections/staff`. The custom collections plugin will automatically convert these into entries on the staff page of the website.

### Hiding/Unhiding Discussion Questions

In `src/lectures/{i}`, change the header in `questions.md` to include or exclude the `discussion_hide_solutions.scss` stylesheet, which hides the answer.

```yaml
extra_css: ["discussion.scss"]
# extra_css: ["discussion.scss", "discussion_hide_solutions.scss"]
```

## Development Conventions

### Markdown

We use MkDocs, which uses Python-Markdown for its Markdown rendering.

- mostly pretty standard markdown implementation with extensions to match
    [PHP markdown extra](https://michelf.ca/projects/php-markdown/extra/)
- see [differences](https://python-markdown.github.io/#differences)

#### Links

All internal links (both relative and absolute) in Markdown get processed by a Markdown extension to

1. check that the file exists
    - else output a warning (which will prevent deployment on master)
2. resolve the file path
    - convert from input (e.g., md, scss, png) to output (e.g., html, css, png)
    - convert any relative links to absolute (i.e., relative to `site_url`/`src` folder
3. prepend `site_url`

Conventions:

- prefer relative links rather than absolute when linking to sibling files
    (e.g., `[project main page](./index.md)`)
  - prefer including `./` to make the relative-ness more obvious
  - (this makes it easier to rename folders)
- prefer absolute links instead of using `../blah` (e.g., `[syllabus](/syllabus.md)`)
  - (this makes it easier to rename folders)
- **NOTE**: relative links are not supported for files in `collections`---they get resolved
    incorrectly.
    Instead, use absolute internal links (e.g., `[syllabus](/syllabus.md)`).
- note: external links are required to link to URLs in `courses.cs.washington.edu` that aren't
    part of the course site (e.g.,
    `[partner form](https://courses.cs.washington.edu/courses/cse373/tools/20su/partner/p1/)`)

#### Code Blocks

- prefer fenced code blocks (using ```)
- indented code blocks always have line numbers enabled
- note: the theme currently doesn't work perfectly with line highlighting---the highlighting ends
    when the text ends, instead of spanning the full line
  - this probably can't be fixed without changing `pymdownx.highlight.linenums_style` back to the
        default, which the theme doesn't currently display properly

#### Other Noteworthy Markdown Extensions

Not a complete list; only the most useful ones

- admonition: use `!!!` to add admonitions (styled as bootstrap alerts by the theme)
- pymdownx.details: use `???` blocks to add details/summary elements

### Noteworthy MkDocs Plugins

- macros: enable Jinja2 support in Markdown files (runs before Markdown)
- custom plugins:
  - collections: the logic behind the collections
  - auto-nav: load all page data earlier and use page metadata to set the nav
    - also removes MkDoc's concept of "sections" from the nav... the plugin and theme probably
            should be rewritten to not do this.
  - sass: compile Sass files when building the site
  - url-validation: this MkDocs plugin replaces the default url resolution Markdown extension
        added by MkDocs with one that outputs absolute links


## Notable Files for Modifying this Template

This is a non-exhaustive list of some of the important files you may be looking for as you **modify the template**. If you are simply changing the information on the site (e.g. for a new quarter), it's unlikely you need to touch these files.

- `/src/index.html`: This enormous file is where all the logic for rendering the course calendar is stored, all done with the Jinja2 templating language.
- `/theme/css/base.scss`: Global styles. Page-specific styles are stored in `/src/*.scss`, notably including `schedule.scss` for the calendar.
- `/mkdocs.yml`: Global configurations (includes google analytics, external links in sidebar, acronyms to style).
- `/data/vars.yml`: Quarter-specific URLs like Gradescope and Canvas (not used in many places, if at all).
- `/main.py`: Place python functions here to make them available in template files. Used extensively in `/src/index.html`.
- `/theme/base.html`: The base template of every page, including navigation
- `/theme/content.html`: The wrapper template around content, including page title, etc.
- `/theme/no-toc.html` and `/theme/no-toc-content.html`: The templates for pages without table of contents (e.g. the home page). Extends `base.html`! Look here if you make changes to `base.html` that don't seem to be appearing on the home page.
- `/theme/nav.html`: Overall navigation template, which includes the navigation for mobile.
- `/includes/announcement.html` and `/includes/staffer.html`: Templates for announcements and staffers. These are in their own location because they are rendered via the `/collections/` system, which renders all files within a subfolder.

## Acknowledgements

This website was originally developed by Brian Chan, Maia Xiao, and Aaron Johnston in 20su. Updates by Hunter Schafer in 20au, and some more updates by Matt Wang across 23au-24su.
