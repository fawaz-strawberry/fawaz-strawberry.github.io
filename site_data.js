
mega_holder = {
    "research":[{"title":"this is research"}, {"date":"12/20/1999"}, {"subtitle":"section1"}, {"information":"random insightful information"}, {"image":"NN_Creator.PNG"}, {"image":"spectogram.PNG"}],
    "musicGenerator":[{"title":"AI Music Generation"}, {"date":"05/02/2021"}, {"image":"spectogram.PNG"}, {"subtitle":"Premise"}, {"information":"Music is a source of happiness for many people throughout the world. This project thus aims to develop a way of rapidly generating great music for anyone to listen to for an extremely cheap cost. The implications of a fully functioning version could even create ripples throughout the entire music industry.\
    "}, {"subtitle":"Implementation"}],
    "ciderTruck":[{"title":"Cider Truck"}, {"date":"02/15/2020"}, {"game":"https://i.simmer.io/@BubbleMagic45/cider-truck"}, {"subtitle":"A Fun Endless Driver"}, {"information":"Cider Truck is a game created in Unity inspired by the Cybertruck. The goal is to survive as long as possible as you drive an endless road with various obstacles. The game has various features and functionalities allowing players to customize their trucks.\
     Above you can try a demo of the game where you use the arrow keys to turn left and right and the space bar to activate your boost. Note: This game was initially designed for a smartphone so you may find bugs in the computer edition."}, {"subtitle":"Creation Process"}, {"information":"Everything from the models, game logic, and AI was created by me. The only things I got else where were the skybox, music, and various textures. The game was also\
     designed with future growth in mind. To create new models to drive in is as simple as uploading a new model and modifying a few variables to account for wheel width and collision boxes. The most difficult part about this game was the controls as fine tuning them to feel 'right' for the user is always a challenge."}, {"subtitle": "Lessons & Future"}, {"information": "While the idea of the game was definitely fun I believe this type of control\
     scheme was not well suited for a smart phone. People often swiped expecting the vehicle to stick to lanes or turn more aggresively. It was quite funny actually watching people struggle. That being said I do have plans to build a new game in the future which is less restricted to an endless runner but instead allows a player to explore an open world. Bringing that experience to a smartphone would be an absolute dream."}]
}


function getJSON(title)
{
    return mega_holder[title]
}