#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galaxy_project.settings')
django.setup()

from learning_path.models import Role, CourseNode

def create_detailed_courses():
    # Get or create roles
    frontend_role, _ = Role.objects.get_or_create(
        name='Frontend',
        defaults={'description': 'Frontend development with modern web technologies'}
    )
    
    backend_role, _ = Role.objects.get_or_create(
        name='Backend',
        defaults={'description': 'Backend development with server-side technologies'}
    )

    # Clear existing courses
    CourseNode.objects.all().delete()

    # ===== FRONTEND COURSES =====
    
    # 1. HTML Fundamentals
    html_fundamentals = CourseNode.objects.create(
        title='HTML Fundamentals',
        description='Learn the basics of HTML markup',
        content='''
# HTML Fundamentals

## What you'll learn:
- HTML document structure
- Semantic HTML elements
- Forms and input types
- Accessibility basics

## Key Topics:
1. **Document Structure**
   - DOCTYPE declaration
   - HTML, head, and body elements
   - Meta tags and SEO basics

2. **Semantic Elements**
   - Header, nav, main, section, article
   - Footer, aside, figure
   - Why semantic HTML matters

3. **Forms and Inputs**
   - Form validation
   - Input types (text, email, password, etc.)
   - Select dropdowns and textareas

4. **Accessibility**
   - ARIA labels and roles
   - Alt text for images
   - Keyboard navigation
        ''',
        course_url='https://developer.mozilla.org/en-US/docs/Learn/HTML',
        role=frontend_role,
        position_x=-20, position_y=0, position_z=0
    )

    # 2. CSS Styling
    css_styling = CourseNode.objects.create(
        title='CSS Styling',
        description='Master CSS for beautiful web design',
        content='''
# CSS Styling

## What you'll learn:
- CSS selectors and specificity
- Box model and layout
- Flexbox and Grid
- Responsive design

## Key Topics:
1. **CSS Fundamentals**
   - Selectors and specificity
   - Box model (margin, border, padding)
   - Colors and typography

2. **Layout Systems**
   - Flexbox for 1D layouts
   - CSS Grid for 2D layouts
   - Positioning (relative, absolute, fixed)

3. **Responsive Design**
   - Media queries
   - Mobile-first approach
   - Viewport meta tag

4. **Advanced CSS**
   - CSS variables (custom properties)
   - Animations and transitions
   - CSS preprocessors (Sass/SCSS)
        ''',
        course_url='https://developer.mozilla.org/en-US/docs/Learn/CSS',
        role=frontend_role,
        position_x=-10, position_y=0, position_z=0
    )

    # 3. JavaScript Basics
    js_basics = CourseNode.objects.create(
        title='JavaScript Basics',
        description='Learn JavaScript programming fundamentals',
        content='''
# JavaScript Basics

## What you'll learn:
- Variables and data types
- Functions and scope
- DOM manipulation
- Event handling

## Key Topics:
1. **JavaScript Fundamentals**
   - Variables (let, const, var)
   - Data types (string, number, boolean, object, array)
   - Operators and expressions

2. **Functions and Scope**
   - Function declarations and expressions
   - Arrow functions
   - Scope (global, function, block)
   - Closures

3. **DOM Manipulation**
   - Selecting elements
   - Modifying content and attributes
   - Creating and removing elements
   - Event listeners

4. **Modern JavaScript**
   - ES6+ features
   - Promises and async/await
   - Modules and imports
        ''',
        course_url='https://developer.mozilla.org/en-US/docs/Learn/JavaScript',
        role=frontend_role,
        position_x=0, position_y=0, position_z=0
    )

    # 4. React Framework
    react_framework = CourseNode.objects.create(
        title='React Framework',
        description='Build modern UIs with React',
        content='''
# React Framework

## What you'll learn:
- React components and JSX
- State and props management
- Hooks and functional components
- React ecosystem

## Key Topics:
1. **React Fundamentals**
   - Components and JSX
   - Props and state
   - Component lifecycle
   - Event handling

2. **Hooks and Modern React**
   - useState and useEffect
   - useContext and useReducer
   - Custom hooks
   - Performance optimization

3. **State Management**
   - Redux and Redux Toolkit
   - Context API
   - State management patterns
   - Data fetching

4. **React Ecosystem**
   - React Router for navigation
   - Styled Components
   - Testing with Jest and React Testing Library
   - Build tools (Vite, Webpack)
        ''',
        course_url='https://react.dev/learn',
        role=frontend_role,
        position_x=10, position_y=0, position_z=0
    )

    # 5. Advanced Frontend
    advanced_frontend = CourseNode.objects.create(
        title='Advanced Frontend',
        description='Master advanced frontend concepts',
        content='''
# Advanced Frontend

## What you'll learn:
- Performance optimization
- Testing and debugging
- Build tools and deployment
- Modern web APIs

## Key Topics:
1. **Performance Optimization**
   - Code splitting and lazy loading
   - Bundle optimization
   - Image optimization
   - Caching strategies

2. **Testing and Quality**
   - Unit testing with Jest
   - Integration testing
   - E2E testing with Cypress
   - Code quality tools (ESLint, Prettier)

3. **Build and Deploy**
   - Webpack configuration
   - CI/CD pipelines
   - Static site generation
   - Progressive Web Apps (PWA)

4. **Modern Web APIs**
   - Service Workers
   - WebSockets
   - WebRTC
   - WebAssembly
        ''',
        course_url='https://web.dev/learn/',
        role=frontend_role,
        position_x=20, position_y=0, position_z=0
    )

    # ===== BACKEND COURSES =====
    
    # 1. Python Fundamentals
    python_fundamentals = CourseNode.objects.create(
        title='Python Fundamentals',
        description='Learn Python programming basics',
        content='''
# Python Fundamentals

## What you'll learn:
- Python syntax and data types
- Control structures and functions
- Object-oriented programming
- File handling and modules

## Key Topics:
1. **Python Basics**
   - Variables and data types
   - Control structures (if, for, while)
   - Functions and scope
   - Error handling with try/except

2. **Data Structures**
   - Lists, tuples, dictionaries
   - Sets and comprehensions
   - String manipulation
   - Collections module

3. **Object-Oriented Programming**
   - Classes and objects
   - Inheritance and polymorphism
   - Encapsulation and abstraction
   - Magic methods

4. **Python Ecosystem**
   - Virtual environments
   - Package management with pip
   - Code organization and modules
   - Documentation and testing
        ''',
        course_url='https://docs.python.org/3/tutorial/',
        role=backend_role,
        position_x=-20, position_y=0, position_z=20
    )

    # 2. Django Framework
    django_framework = CourseNode.objects.create(
        title='Django Framework',
        description='Build web applications with Django',
        content='''
# Django Framework

## What you'll learn:
- Django project structure
- Models and database ORM
- Views and URL routing
- Templates and forms

## Key Topics:
1. **Django Basics**
   - Project and app structure
   - Settings configuration
   - URL patterns and views
   - Templates and template inheritance

2. **Models and Database**
   - Model fields and relationships
   - Database migrations
   - QuerySet API
   - Model forms and validation

3. **Advanced Django**
   - Class-based views
   - Django REST Framework
   - Authentication and permissions
   - Caching and optimization

4. **Deployment and Security**
   - Static files and media
   - Environment variables
   - Security best practices
   - Deployment to production
        ''',
        course_url='https://docs.djangoproject.com/en/stable/intro/tutorial01/',
        role=backend_role,
        position_x=-10, position_y=0, position_z=20
    )

    # 3. API Development
    api_development = CourseNode.objects.create(
        title='API Development',
        description='Design and build RESTful APIs',
        content='''
# API Development

## What you'll learn:
- REST API principles
- API design patterns
- Authentication and security
- API documentation

## Key Topics:
1. **REST Fundamentals**
   - HTTP methods and status codes
   - Resource-oriented design
   - Stateless architecture
   - RESTful URL patterns

2. **API Design**
   - Request/response formats
   - Error handling
   - Pagination and filtering
   - Versioning strategies

3. **Authentication & Security**
   - Token-based authentication
   - OAuth 2.0 and JWT
   - API rate limiting
   - CORS and security headers

4. **API Documentation**
   - OpenAPI/Swagger
   - Postman collections
   - API testing strategies
   - Developer experience
        ''',
        course_url='https://restfulapi.net/',
        role=backend_role,
        position_x=0, position_y=0, position_z=20
    )

    # 4. Database Design
    database_design = CourseNode.objects.create(
        title='Database Design',
        description='Master database design and optimization',
        content='''
# Database Design

## What you'll learn:
- Database design principles
- SQL and query optimization
- NoSQL databases
- Data modeling

## Key Topics:
1. **Database Fundamentals**
   - ACID properties
   - Normalization and denormalization
   - Indexing strategies
   - Transaction management

2. **SQL Mastery**
   - Complex queries and joins
   - Subqueries and CTEs
   - Stored procedures
   - Query optimization

3. **NoSQL Databases**
   - Document databases (MongoDB)
   - Key-value stores (Redis)
   - Graph databases (Neo4j)
   - When to use NoSQL

4. **Data Modeling**
   - Entity-relationship diagrams
   - Data warehouse design
   - Big data considerations
   - Database migration strategies
        ''',
        course_url='https://www.postgresql.org/docs/current/tutorial.html',
        role=backend_role,
        position_x=10, position_y=0, position_z=20
    )

    # 5. DevOps & Deployment
    devops_deployment = CourseNode.objects.create(
        title='DevOps & Deployment',
        description='Deploy and maintain applications',
        content='''
# DevOps & Deployment

## What you'll learn:
- Containerization with Docker
- CI/CD pipelines
- Cloud deployment
- Monitoring and logging

## Key Topics:
1. **Containerization**
   - Docker containers and images
   - Docker Compose
   - Container orchestration
   - Microservices architecture

2. **CI/CD Pipelines**
   - GitHub Actions
   - Automated testing
   - Deployment automation
   - Blue-green deployments

3. **Cloud Platforms**
   - AWS, Azure, Google Cloud
   - Serverless computing
   - Cloud-native applications
   - Infrastructure as Code

4. **Monitoring & Operations**
   - Application monitoring
   - Log aggregation
   - Performance metrics
   - Incident response
        ''',
        course_url='https://docs.docker.com/get-started/',
        role=backend_role,
        position_x=20, position_y=0, position_z=20
    )

    # ===== SET UP PREREQUISITES =====
    
    # Frontend prerequisites
    css_styling.prerequisites.add(html_fundamentals)
    js_basics.prerequisites.add(html_fundamentals)
    react_framework.prerequisites.add(js_basics, css_styling)
    advanced_frontend.prerequisites.add(react_framework)

    # Backend prerequisites
    django_framework.prerequisites.add(python_fundamentals)
    api_development.prerequisites.add(django_framework)
    database_design.prerequisites.add(python_fundamentals)
    devops_deployment.prerequisites.add(api_development, database_design)

    print("✅ Detailed courses created successfully!")
    print(f"Frontend courses: {CourseNode.objects.filter(role=frontend_role).count()}")
    print(f"Backend courses: {CourseNode.objects.filter(role=backend_role).count()}")

if __name__ == '__main__':
    create_detailed_courses() 