from classes import *

network1 = SocialNetwork("Jackchat")

network1.register_user("jack", "jack@email.com", "My name is Jack!")
network1.register_user("paige", "paige@email.com", "My name is Paige!")
network1.register_user("will", "will@email.com", "My name is Will!")
network1.register_user("krista", "krista@email.com", "My name is Krista!")
network1.register_user("eric", "eric@email.com", "My name is Eric!")

network1.users["jack"].follow(network1.users["paige"])
network1.users["jack"].follow(network1.users["will"])
network1.users["jack"].follow(network1.users["eric"])
network1.users["jack"].follow(network1.users["krista"])

network1.users["jack"].create_post("I am Jack")
network1.users["paige"].create_post("I am paige")
network1.users["paige"].create_post("I go to Penn State")
network1.users["will"].create_post("I am will")
network1.users["will"].create_post("I am a nurse")
network1.users["krista"].create_post("I am krista")
network1.users["eric"].create_post("I am eric")
network1.users["eric"].create_post("I drive a BMW")
network1.users["jack"].create_post("I am Jack. #swag #Lola")
network1.users["jack"].create_post("I made Jackgram. #swag #Lola")

network1.users["jack"].posts[0].like("eric")
network1.users["jack"].posts[0].like("paige")
network1.users["jack"].posts[0].like("will")
network1.users["jack"].posts[0].like("krista")

network1.users["jack"].posts[0].add_comment("eric", "nice")