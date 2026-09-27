# DevHorizon - Standalone Blog Subapp

> A modular Django blogging system built as the first standalone piece of my larger DevHorizon project.

DevHorizon is my portfolio, blog, and social publishing project. i decided to build the blog separately first: get the publishing system working properly, keep it modular, and integrate it into the main platform once the standalone version is complete.

i have intentionally focused on the core blogging experience first. it covers the mechanics that actually matter for a usable publishing platform — accounts, posts, categories, search, comments, authentication, and content management — while leaving room for a much larger feature set later.

the entirety follows modular architecture and DRY approach as recommended by the django philosophy.

## Current Status

**~85% complete**

the standalone blog is being finished as a self-contained application before it is folded into the main DevHorizon project.

the project started from a Django blogging tutorial and has been adapted substantially around the way i want the platform to work, although on the later phases as of course deviated significantly and has major differences. read more below.

## Workflow and Features

### Publishing

- Create, edit, and delete blog posts
- Automatic slug generation for posts
- Author assignment through the authenticated user
- Draft/publishing workflow foundations
- Rich text content editing
- Featured and recent post sections
- Posts organized by category
- Individual post pages
- Search across blog content

### Accounts

- User registration
- Login and logout
- Authentication-protected actions
- User-linked content and authorship

### Categories & Content Organization

- Create and manage categories
- Associate posts with categories
- Browse posts by category
- Category-aware blog navigation

### Comments

- Authenticated users can leave comments
- Comments are associated with blog posts and users
- Comment display is integrated into the post experience

### Admin & Management

- Django admin support
- Content management through structured views and forms
- Clean separation between the public blog and management functionality
- Reusable templates through template inheritance
- Context processors for shared site data

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django |
| Language | Python |
| Database | SQLite during development / configurable database |
| Templates | Django Templates |
| Styling | Bootstrap |
| Authentication | Django Authentication |
| Content Management | Django Models, Forms & Admin |
| Version Control | Git |

tbh the stack is deliberately straightforward at this stage. The goal is to keep the core application easy to understand, modify, and eventually plug into the wider DevHorizon platform.

## Project Direction

Once the blog is complete, it will be integrated into the main platform so that the portfolio, personal site, publishing system, and future social features can share the same ecosystem.

That gives the project two useful boundaries:

```text
Standalone Blog
      │
      │ complete + stabilize
      ▼
DevHorizon Core
      │
      ├── Portfolio
      ├── Blog
      ├── Social / Community Features
      └── Future Platform Features
```

The blog therefore needs to stay reasonably modular. Features are being developed so they can be reused or extended rather than being tightly coupled to the current standalone presentation.

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

or perhaps for Windows:

```shell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Development Notes

The project uses Django's standard application structure, which keeps the core pieces easy to extend:

- Models handle persistent content and relationships.
- Views handle application logic and request flow.
- Forms handle user input.
- Templates handle presentation.
- Django's authentication system handles user access.
- The admin interface provides a convenient management layer during development.

The application also makes use of template inheritance and shared context so common site elements do not need to be duplicated across every page.

### Why Build the Blog First?

The blog is a good first module for DevHorizon because it touches a lot of the fundamentals that the larger platform will eventually need:

```text
Users
  ↓
Authentication
  ↓
Content ownership
  ↓
CRUD operations
  ↓
Relationships
  ↓
Search / filtering
  ↓
Comments & interaction
  ↓
Administration
```

Finishing these pieces independently makes the eventual integration much cleaner.

### Roadmap

The current release covers the core blogging workflow. The next phase will focus on making the system feel more like a proper publishing platform rather than stopping at CRUD functionality.

Planned areas include:

- Better post discovery and navigation
- More flexible author profiles
- Improved editing and publishing workflows
- Richer commenting and interaction features
- Post metadata and sharing
- Better moderation and access control
- Performance and query improvements
- Production deployment and hardening
- Integration with the main DevHorizon application

Some of these will become separate modules as the platform grows.

#### Inspiration

The initial implementation was heavily inspired by a Django blogging tutorial covering the construction of a complete blogging platform, including models, categories, authentication, search, comments, dashboards, permissions, and deployment.

The tutorial provided the starting point; the project has since been adapted around DevHorizon's own structure and publishing model.

---
