from data import *

# Register users for Jackify
Jackify.register_user("Jack", "jhohman@gmail.com", "free")
Jackify.register_user("Lola", "lhohman@gmail.com", "free")
Jackify.register_user("Paige", "phohman@gmail.com", "free")
Jackify.register_user("Will", "whohman@gmail.com", "free")
Jackify.register_user("Eric", "ehohman@gmail.com", "free")
Jackify.register_user("Krista", "khohman@gmail.com", "free")

# Add artists to Jackify
for artist in (
    Muse,
    GreenDay,
    Drake,
    Future,
    LukeCombs,
    TravisScott,
    FrankOcean,
    SwaeLee,
    KidCudi,
    JamesBlake,
    PhilipBailey,
    JuiceWRLD,
    SheckWes,
    TheWeeknd,
    TwentyOneSavage,
    Gunna,
    Nav,
    DonToliver,
    Quavo,
    Takeoff
):
    Jackify.add_artist(artist)

# Add albums to Jackify
for album in (
    Absolution,
    AmericanIdiot,
    WhatATimeToBeAlive,
    Dookie,
    GettinOld,
    Astroworld
):
    Jackify.add_album(album)

# Add all songs to Jackify
for song in all_songs:
    Jackify.add_song(song)

# Add songs to Absolution
for song in (
    Muse_Intro,
    Muse_ApocalypsePlease,
    Muse_TimeIsRunningOut,
    Muse_SingForAbsolution,
    Muse_StockholmSyndrome,
    Muse_FallingAwayWithYou,
    Muse_Interlude,
    Muse_Hysteria,
    Muse_Blackout,
    Muse_ButterfliesAndHurricanes,
    Muse_TheSmallPrint,
    Muse_Endlessly,
    Muse_ThoughtsOfADyingAtheist,
    Muse_RuledBySecrecy
):
    Jackify.artists["Muse"].albums["Absolution"].add_song(song)

# Add songs to American Idiot
for song in (
    GreenDay_AmericanIdiot,
    GreenDay_JesusOfSuburbia,
    GreenDay_Holiday,
    GreenDay_BoulevardOfBrokenDreams,
    GreenDay_AreWeTheWaiting,
    GreenDay_StJimmy,
    GreenDay_GiveMeNovacaine,
    GreenDay_ShesARebel,
    GreenDay_ExtraordinaryGirl,
    GreenDay_Letterbomb,
    GreenDay_WakeMeUpWhenSeptemberEnds,
    GreenDay_Homecoming,
    GreenDay_Whatshername
):
    Jackify.artists["Green Day"].albums["American Idiot"].add_song(song)

# Add songs to What a Time to Be Alive
for song in (
    DrakeFuture_DigitalDash,
    DrakeFuture_BigRings,
    DrakeFuture_LiveFromTheGutter,
    DrakeFuture_DiamondsDancing,
    DrakeFuture_Scholarships,
    DrakeFuture_PlasticBag,
    DrakeFuture_ImThePlug,
    DrakeFuture_ChangeLocations,
    DrakeFuture_Jersey,
    DrakeFuture_30For30Freestyle
):
    Jackify.artists["Drake"].albums["What a Time to Be Alive"].add_song(song)

# Add songs to Dookie
for song in (
    GreenDay_Burnout,
    GreenDay_HavingABlast,
    GreenDay_Emenius,
    GreenDay_InTheEnd,
    GreenDay_Longview,
    GreenDay_WelcomeToParadise,
    GreenDay_PullingTeeth,
    GreenDay_BasketCase,
    GreenDay_SheDookie,
    GreenDay_Sassafras,
    GreenDay_WhenIComeAround,
    GreenDay_ComingClean,
    GreenDay_NickyNine,
    GreenDay_FOD,
    GreenDay_AllByMyself
):
    Jackify.artists["Green Day"].albums["Dookie"].add_song(song)

# Add songs to Gettin' Old
for song in (
    LukeCombs_GrowinUp,
    LukeCombs_HannahFord,
    LukeCombs_Back40,
    LukeCombs_YouFound,
    LukeCombs_BeerBand,
    LukeCombs_Still,
    LukeCombs_SeeMeNow,
    LukeCombs_Joe,
    LukeCombs_SongWasBorn,
    LukeCombs_MySong,
    LukeCombs_WildThings,
    LukeCombs_LoveYou,
    LukeCombs_TakeYou,
    LukeCombs_FastCar,
    LukeCombs_Tattoo,
    LukeCombs_5Leaf,
    LukeCombs_Fox,
    LukeCombs_ThePart
):
    Jackify.artists["Luke Combs"].albums["Gettin' Old"].add_song(song)

# Add songs to Astroworld
for song in (
    TravisScott_Stargazing,
    TravisScott_Carousel,
    TravisScott_SickoMode,
    TravisScott_RIP,
    TravisScott_StopTrying,
    TravisScott_NoBS,
    TravisScott_Skeletons,
    TravisScott_WakeUp,
    TravisScott_5Percent,
    TravisScott_NC17,
    TravisScott_Astrothunder,
    TravisScott_Yosemite,
    TravisScott_CantSay,
    TravisScott_Who,
    TravisScott_Butterfly,
    TravisScott_Houstonfornication,
    TravisScott_Coffee
):
    Jackify.artists["Travis Scott"].albums["Astroworld"].add_song(song)

# Print songs in album
# for song in Jackify.artists["Luke Combs"].albums["Gettin' Old"].songs:
#     print(song.title)

# Print all songs
# for key, value in Jackify.songs.items():
#     print(key)

# Print all artist songs
# for song in Jackify.artists["Green Day"].songs:
#     print(song.artist)
#     print(song.title)

# Playlist
# Jackify.users["Jack"].create_playlist("Jack's Playlist", True, "Description")
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(Muse_Hysteria)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(GreenDay_Holiday)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(LukeCombs_FastCar)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(GreenDay_AmericanIdiot)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(TravisScott_NoBS)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(GreenDay_WhenIComeAround)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(GreenDay_BasketCase)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(TravisScott_Stargazing)
# Jackify.users["Jack"].playlists["Jack's Playlist"].add_song(TravisScott_SickoMode)


# for name, playlist in Jackify.users["Jack"].playlists.items():
#     print(name)
#     for char in range(len(name)):
#         print("-", end="")
#     print()
#     for song in playlist.songs:
#         print(song.title)

# Jackify.users["Jack"].play_song(Muse_Hysteria)
# Jackify.users["Jack"].play_song(Muse_Hysteria)
# Jackify.users["Jack"].play_song(GreenDay_Holiday)
# Jackify.users["Jack"].play_song(GreenDay_WhenIComeAround)
# Jackify.users["Jack"].play_song(LukeCombs_FastCar)
# Jackify.users["Jack"].play_song(LukeCombs_FastCar)
# Jackify.users["Jack"].play_song(LukeCombs_FastCar)
# Jackify.users["Jack"].play_song(LukeCombs_FastCar)
# Jackify.users["Jack"].play_song(LukeCombs_FastCar)
# Jackify.users["Jack"].play_song(TravisScott_SickoMode)
# Jackify.users["Jack"].play_song(TravisScott_SickoMode)
# Jackify.users["Jack"].play_song(GreenDay_AmericanIdiot)
# Jackify.users["Jack"].play_song(GreenDay_BasketCase)
# Jackify.users["Jack"].play_song(LukeCombs_WildThings)
# Jackify.users["Jack"].play_song(TravisScott_NoBS)
# Jackify.users["Jack"].play_song(TravisScott_Stargazing)
# Jackify.users["Jack"].play_song(GreenDay_AreWeTheWaiting)
# Jackify.users["Jack"].play_song(GreenDay_Burnout)
# Jackify.users["Jack"].play_song(Muse_Hysteria)
# Jackify.users["Jack"].play_song(DrakeFuture_DigitalDash)
# Jackify.users["Jack"].play_song(DrakeFuture_LiveFromTheGutter)

# radio_station = Jackify.generate_radio_station(Muse_Hysteria)
# for song in radio_station:
#     print(song.title)

# print(Jackify.songs["Muse", "Hysteria"].tags)
# print(Jackify.songs["Muse", "Hysteria"].genre)

# played = set()

# for song in Jackify.songs.values():
#     if song not in played:
#         print(song.title)
#         played.add(song)
