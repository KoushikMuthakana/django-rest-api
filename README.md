# Django-Rest_API

Framework: Django Rest framework

Steps to insatll Rest Framework

      pip install djangorestframework
      

User Profile APIs:

      1. Create New Profile
          - Validate Profiel Data
      
      2. List Existing profiles
          - Search for profile
          
      3. View Specific Profile
      
      4.Update Profile of logged user
          - Update name/email address
          - Change Password
          
      5. Delete Profile
      
URLs of APIs:
      
       - /api/profile/  -list all profiles
              - GET (list profiles)
              - POST (Create profile)
       - /api/profile/<profile_id>/  Manage specific profile
              - GET (View specific profile)
              - PUT/PATCH (Update profile)
              - DELETE (Remove profile)
        
