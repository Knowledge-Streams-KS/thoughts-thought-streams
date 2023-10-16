Project Name:
 Thoughts

1 Installation and Setup :

a.Clone this repository to your local machine:
   bash
   git clone <repository-url>

b.Create a virtual environment and activate it:
   python -m venv myenv
   source myenv/bin/activate

c. Install project dependencies:
   pip install -r requirements.txt

d.Configure database settings in settings.py.

e.Run database migrations to create necessary tables:
  python manage.py makemigrations
  python manage.py migrate

f Create a superuser to access the Django admin panel:
  python manage.py createsuperuser

g. Start the development server:
  python manage.py runserver


2 Running the Project :
Access the Django admin panel at /admin and use the superuser credentials to manage users and content.
Visit the homepage at the base URL to learn about the application and register or log in.

3 Make logical and meaningful commits :
Follow the commit guidelines provided in this README.
Submit pull requests for review.

4 Commit Guidelines :
Use descriptive and concise commit messages.
Start with a verb in the present tense (e.g., "Add user registration feature").
Provide detailed information about what the commit accomplishes.

5 Design and Styling:
Use HTML,CSS and Bootstrap and Javascript for front-end design.
Maintain clean and reusable templates with a design hierarchy.
Ensure that header and footer templates are parents to all others where needed.

6 Folder Structure :
Keep the project's folder structure clean and logical.
Organize resources, templates, and static files in a well-formatted manner.

7 Code Comments :
Add comments to your code to explain its functionality.
Make it easy for others to understand your code and contributions.

8 Key Functionalities Of Thoughts Project:

a. User Registration and Login:
Users can sign up for accounts and log in securely to access the platform.

b. User Profiles: 
Each user has a dedicated profile where they can add a bio, profile picture, date of birth, and current city information.

c. Thoughts Posting: 
Users can create thoughts with text, titles, and optional images. Thoughts are displayed in a well-formatted manner.

d. Thought Privacy: 
Thoughts can be set as private or public, giving users control over who can view their content.

e. Comments: 
Users can engage with thoughts by adding comments, fostering discussions and interactions.

f. Sharing:
Users can share public thoughts with other users, extending the reach of interesting content.


g. Search Functionality: 
Users can search for thoughts using keywords, and the system will display relevant thoughts containing the text.

h. Navigation Bar: 
The application features a top navigation bar with icons for easy access to various sections, providing a seamless user experience.

i. Thoughts Shared with the User: 
Users can navigate to a dedicated page to view thoughts shared with them, irrespective of privacy settings. They can comment on and share these thoughts with others if they are public.

