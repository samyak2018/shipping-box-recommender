# AI Usage

## 1. AI Tools Used

I used ChatGPT during this project mainly to understand the requirements, plan the Django project, get guidance during implementation, and debug issues when I got stuck.

## 2. Prompts Used

These are some of the main prompts I used:

1. "I want to build this project step by step. First, help me understand the requirement and suggest how I should approach this project using Django. What models will I need, how should the box selection logic work, what basic validations should I consider, and what should be the overall flow of the application? For now, I want to understand the approach and project structure before starting the implementation."

2. "Okay, I understood the basic approach. Since the assignment also mentions box cost, how should we use cost while selecting the best box? Also, can we now finalize the models and project structure before I start coding?"

3. "Okay, let's start the implementation now. I am using VS Code. Please guide me from the beginning to create the Django project and orders app, including the commands I need to run. After the basic setup, let's create the models we finalized. Explain the steps as we go so I can understand what I am doing."

4. "I noticed that products can currently be added only through Django Admin, while the Create Order page uses the existing products. Why didn't we add an Add Product option in the application? Do you think it's necessary to add this feature, or is Django Admin enough?"

I also used shorter follow-up prompts while implementing individual parts and fixing errors.

## 3. Output Accepted

I used the suggestions that were suitable for the project, such as separating the recommendation logic into a service file, checking dimensions with product rotation, validating weight and volume, considering box cost, and testing the main functionality.

I also followed the suggested Django structure for models, forms, views, URLs, templates, and tests.

## 4. Output Rejected or Modified

I did not use every suggestion as it was given. I kept product and shipping-box management in Django Admin instead of adding separate pages because the main focus of the project is order creation and box recommendation.

I also avoided adding extra features that were not needed. Some code and UI parts were changed while integrating and testing them in my project.

## 5. Mistakes Made by AI

There were a few issues during development. The expected number of tests was different from the number Django actually discovered. I also faced some URL and import errors while connecting different parts of the application.

One test failed because the message expected by the test was different from the message displayed in the template. I checked the test output and corrected the mismatch.

## 6. How I Verified the Final Code

I did not rely only on the suggested code. I tested the recommendation logic through the Django shell and tested the complete order flow in the browser.

I also used Django Admin to check products and shipping boxes and ran Django's system checks and automated tests.

Commands used for verification included:

`python manage.py check`

`python manage.py test`

`python manage.py test --verbosity=2`

The final test suite contains 31 tests, and all tests passed successfully.
