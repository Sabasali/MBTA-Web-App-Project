Team Member: Kimheat and Saba
# MBTA-Web-App-Project

This is the base repository for Web App project. Please read the [instructions](instructions.md) for details.

1. Project Overview:
    The main goal of the project is to return the nearest MBTA station based on the user's input location. Some of the core features I have included include the MBTA's coordinates which are the longtitude and the latitude and whether they have wheelchair assessibility.
   Two of the "wow features" we have included that are interesting are including the arrival time, and making the website more appealing using CSS. 

2. Reflection:

   1) Development Process: I believe that breaking the process into functions went very well. For instance, we break different functions such as get_the_nearest_station, get_lat_lon since they perform a different task that builds up to form this project. Additionally, any time I added a few lines of code, I will test them to ensure that if they are not working, I can catch the mistakes early on. I also enjoy the HTMLportion of the project, ensuring that the website is interactive and cool to look at in the perspective of the users.
   - The most challenging section is getting Flask reporting the information such as the nearest station, the arrival time, and whether or not there are wheelchair accessibility. For a while, whenever I enter the location, none of the information will show up. However, after trials and errors and making sure that I render HTML, I started getting more information on the website. Additionally, I also put my key in gitignore instead of the .env, so that also contributes to the information not being displayed on the site.
   - I approach problem-solving by running the code line by line instead of running the whole code again and again. By commenting on the rest of the code, and run the code line by line, I can easily see where the code went wrong. However, if that does not work well, I also screenshot the issues, and ask chatgpt what went wrong and how I can fix this. (You can check some of the errors we ran into in the screenshot folder).
   - If we were to do the project again, I would try to work on htlm, mbta.py, and Flask at different times instead of working with three files simultaneously. When I worked on them at the same time, I got lost at times and when I ran into errors, I am not sure where the issues are, so I ended up testing all three files, which was very time consuming.
   2) Teamwork and Collaboration: We divided the tasks. Since Kimheat signed up for the API key from MapBox and MBTA, it makes sense for her to do the MBTA.py file and Saba did the Flask.py and the HTML index, since they work together to build the website. Together, Saba and Kimheat finishes off by writing the reflection and write-up. 
   - Our plan did not changed much. Initially, we only planned to make sure that the project does it bare minimum which is to return the nearest MBTA. After that was successful, we also decided to move onto adding more features such as the arrival time and making the website look a bit more appealing.
   - The collaboration was smooth. We could have communicated more, but since we have GitHub, we can see the updated version of our work smoothly.
   3) Learning and Use of AI: I used AI to write helper functions and integrating them into the modules. I know the concept of the project, but translating the tasks into code is a little bit harder to do. Another example why AI was helpful is in debugging. Initially, finding errors myself is easy, but once the code gets long, AI is helping in detecting the errors, which saves some of my time which I use to focus more on the appearance of the website development.
   Some of the things I learn through AI is how to import functions from the MBTA to flask and how to render HTML. Since I have not learned about HTML before, AI also helps me understand the structure of HTML and how they complement the tasks that Flask does. I also learn how to store API_keys and how to use them in the MBTA file. 
    - I use mostly CHATGPT. ChatGPT is clearer in explaining errors especially to beginners, while I find Copilot is a little bit more advanced level. 
    - Some limitations I see specifically in chatGPT is that even though they give me the correct code, but sometimes they ignore the code I already had, so if I want to use their code, I would have to adapt, not ChatGPT adapted to my code. 
    - Although we talked about it in class, I wish I have known to store my API keys in .env instead of .gitignore. The good thing is I have not committed my code, so I was able to correct my mistake. 


   
