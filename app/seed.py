"""Seed file to make sample data for comicswap2 db."""

from models import db, Msg, User, Comic, Offer, Deal, Pedigree
# import Comics-offers
from main import app

with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

############################### USERS ####################################
# If table isn't empty, empty it
User.query.delete()

# Add users
usr1 = User(
    username="magiclar", 
    fname="Larry", 
    lname="Volz", 
    email="imaginologist@gmail.com", 
    confirmation_token="OU812",
    confirmed=False,
    blocked=False,
    role=0,
    mailinglist=True,
    password="testPassword1"
    )

usr2 = User(
    username="comicrodney", 
    fname="Rodney", 
    lname="Chakan", 
    email="something@thecomicswap.com", 
    confirmation_token="ASDF1234",
    confirmed=False,
    blocked=False,
    role=1,
    mailinglist=True,
    password="testPassword2"
    )

# Add new users to session, so they'll persist
db.session.add(usr1)
db.session.add(usr2)

############################### MESSAGES ####################################
# If table isn't empty, empty it
Msg.query.delete()

# Add messages
msg1 = Msg(to_id=1, from_id=2, subject="first db test of msgs", content="this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

msg2 = Msg(to_id=2, from_id=1, subject="NOT FOR USER #1 - 2nd db test of msgs", content="MORE TEXT!!!  this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

msg3 = Msg(to_id=1, from_id=2, subject="2nd msg for user 1", content="this would be a great place for some lorem ipsum.  But I'll just type up some random content instead.  Okay, that should be enough.", read=False, attachments="{'http://www.test.com', 'http://www.test2.com'}")

# Add new messages to session, so they'll persist
db.session.add(msg1)
db.session.add(msg2)
db.session.add(msg3)


############################### OFFERS ####################################
# If table isn't empty, empty it
Offer.query.delete()

# Add offers
ofr1 = Offer(title="Fantastic 4 for your Batman",num_comics_offered=1,user_offering=2,user_owner=1,owner_response=0,deal_id=0,payment_offer=0,additional_terms="Contingent on pedigree being confirmed.")

ofr2 = Offer(title="Captain America for your Amazing Spiderman",num_comics_offered=1,user_offering=1,user_owner=2,owner_response=0,deal_id=0,payment_offer=0,additional_terms="Looking forward to the deal.")

ofr3 = Offer(title="Superman for your Doctor Strange",num_comics_offered=1,user_offering=2,user_owner=1,owner_response=0,deal_id=0,payment_offer=0,additional_terms="Assuming it's not cursed by an evil trans-dimensional demon.")


# Add new messages to session, so they'll persist
db.session.add(ofr1)
db.session.add(ofr2)
db.session.add(ofr3)

db.session.commit()


 ############################# comics-offers ##############################
#  TODO: For future development - so people can trade more than one comic at a time
# Comics_offers.query.delete()

# c_o1 = Comics_offers(offer_id=1, comic_id=)



############################### COMICS ####################################
# If table isn't empty, empty it
Comic.query.delete()

# Add messages
comic1 = Comic(owner_id=1, title="Batman", issue_num=265, cgc_grade=9.6,assessed_value=40.0, assessed_source="CGC", thumbnail="../static/images/batman-p-500.jpg", cover_pic="../static/images/batman-p-1080.jpg", back_cover_pic="", extra_media="", publisher="DC", year=1975, notes="Title is Batman's greatest failure", signed=True, pedigree=1, location=0)

comic2 = Comic(owner_id=1, title="Captain America", issue_num=100, cgc_grade=9.9,assessed_value=5400, assessed_source="CGC", thumbnail="../static/images/captain_america-p-250.jpg", cover_pic="../static/images/captain_america-p-1080.jpg", back_cover_pic="", extra_media="", publisher="Marvel", year=1968, notes="Title is 'Big Premier Issue'", signed=False, pedigree=2, location=0)

comic3 = Comic(owner_id=1, title="Doctor Strange", issue_num=50, cgc_grade=9.9,assessed_value=9.99, assessed_source="CGC", thumbnail="../static/images/Dr_strange-p-250.jpg", cover_pic="../static/images/Dr_strange-p-100.jpg", back_cover_pic="", extra_media="", publisher="Marvel", year=1993, notes="Holographic giant issue Guest starring Ghost Rider, Hulk and Silver Surfer'", signed=False, pedigree=3, location=0)

comic4 = Comic(owner_id=2, title="Fantastic 4", issue_num=52, cgc_grade=9.9,assessed_value=4000, assessed_source="CGC", thumbnail="../static/images/fantastic4_and_black_panther-p-250.jpg", cover_pic="../static/images/fantastic4_and_black_panther-p-1080.jpg", back_cover_pic="", extra_media="", publisher="Marvel", month="July", year=1966, notes="Featuring Black Panther", signed=False, pedigree=4, location=0)

comic5 = Comic(owner_id=2, title="Amazing Fantasy Featuring Spider-Man", issue_num=15, cgc_grade=9.0,assessed_value=1100000, assessed_source="CGC", thumbnail="../static/images/spider_man_coolest_pic-p-250.jpg", cover_pic="../static/images/spider_man_coolest_pic.jpg", back_cover_pic="", extra_media="", publisher="Marvel", month="August", year=1962, notes="First appearance of Spider-Man", signed=False, pedigree=5, location=0)

comic6 = Comic(owner_id=2, title="Action Comics featuring Superman", issue_num=419, cgc_grade=9.0,assessed_value=6.0, assessed_source="CGC", thumbnail="../static/images/superman-p-250.jpg", cover_pic="../static/images/superman-p-1080.jpg", back_cover_pic="", extra_media="", publisher="Marvel", month="August", year=1972, notes="First appearance of Spider-Man", signed=False, pedigree=5, location=0)

# Add new messages to session, so they'll persist
db.session.add(comic1)
db.session.add(comic2)
db.session.add(comic3)
db.session.add(comic4)
db.session.add(comic5)
db.session.add(comic6)


# Commit--otherwise, this never gets saved!
db.session.commit()


############################### DEALS ####################################
# If table isn't empty, empty it
Deal.query.delete()

# Add deals
deal1 = Deal(date_of_agreement="2022-11-10 17:00:00.0", amt_owed_seller=0, amt_paid_to_seller=0, amt_owed_comicswap=12.50, amt_paid_comicswap=0, payment_status=0, offer_id=1, delivery_status=0, comic_condition=0)


# Add new messages to session, so they'll persist
db.session.add(deal1)
# db.session.add(deal2)
# db.session.add(deal3)

# Commit--otherwise, this never gets saved!
db.session.commit()


############################### PEDIGREES ####################################
# If table isn't empty, empty it
Pedigree.query.delete()

# Add offers
ped1 = Pedigree(title="Allentown", description="Purchased by Jim Payette and Stephen Fishler in 1987, the Allentowns only numbered 135 comics, but contained some of the highest graded copies of several key issues such as Detective Comics #27, Marvel Comics #1, Captain America #1 and Batman #1. The original owner had discovered his mother had saved his small collection when he found them in her closet. His acquaintance, a local antique dealer contacted six comic book dealers to place bids, with Payette and Fishler bidding the highest. Even though the comics do not exhibit any distinctive markings, nearly every copy has retained its provenance.", media="../static/images/pedigrees/allentown.jpg")

ped2 = Pedigree(title="Aurora", description="In the fall of 1996 in Aurora, Colorado, a young man carrying a bag of comic books walked into Castaway Comics, owned by Dennis Grimm. It was the first of several bags that eventually accumulated into a large collection of over 2,000 comics - now known as the Aurora Collection. The collection came from the man's grandfather and covered many genres from the late '40s to the early '50s, with horror, western, crime, good-girl and science fiction being the most prominent genres. Most copies exhibit a distributor code written in grease pencil on the front cover.", media="../static/images/pedigrees/aurora.jpg")

ped3 = Pedigree(title="Bethlehem", description="This massive collection of 18,000 comic books was assembled by Stanley Pachon in Bethlehem, PA, and stretched from 1950 into the Silver Age. It contained many popular 50's runs and a score of Marvel and DC keys. After Pachon passed away, the collection was sold to Joe Rainone and Phil Weiss in 1990. The Bethlehems were one of the first pedigreed collections to contain Silver Age, and many are easily identifiable by a store stamp found on the back covers.", media="../static/images/pedigrees/bethlehem.jpg")

ped4 = Pedigree(title="Big Apple", description="The Big Apple collection is unique in a few ways. It was assembled by an African American named James Hilton and its span is huge, beginning in 1939 and continuing 30 years to the end of the Silver Age. Even though Hilton passed away in 1968, it wasn't until 1993 that his nephew Ron discovered the collection in the family home. A part of the collection was ultimately sold through Christie's Auction House between 1994 and 2000. The Golden Age portion of the collection has whiter paper, particularly from 1944, and they exhibit a distinctive pencil mark on the front covers.", media="../static/images/pedigrees/bigapple.jpg")

ped5 = Pedigree(title="Billy Wrighte", description="One of the most recent Golden Age pedigrees recognized by CGC, it covers the 1936-1941 period numbering approximately 340 comics that included 67 #1 issues, an Action Comics #1 among them. Wright was nine years old when he started to amass his collection, passing away in 1994. His books were discovered in the basement after his wife also passed in 2011. Heritage auctioned the collection that same year, which sold for $3.4 million. Even though his name is written on a few covers, the collection does not have any distinctive markings.", media="../static/images/pedigrees/billywright.jpg")

ped6 = Pedigree(title="Boston", description="Named for the city from which Bechara Maalouf hails, he unveiled a box of very high grade Silver Age books at a New York show in the '90s. An older couple began coming to the same show with similar boxes, who dealers realized was the source of Bechara's find. Mainly consisting of comics from 1964 to 1975, the Boston collection contained many duplicates, but did not exhibit any identifiable markings on the covers. Of note, the Fantastic Four #55 graded CGC 9.9, one of the few 9.9 grades assigned to a Silver Age comic book.", media="../static/images/pedigrees/boston.jpg")

ped7 = Pedigree(title="Bowling Green", description="This collection originated from Bowling Green, Kentucky, and first surfaced for sale in the 1999 Sotheby's comic auction. It consisted of Marvel and DC issues spanning 1960-1980. Although some of the earlier issues were lower in grade, the condition improved considerably after 1964. Most copies exhibit a date stamp on the front cover.", media="../static/images/pedigrees/bowlinggreen.jpg")

ped8 = Pedigree(title="Carson City", description="One of four Golden Age pedigrees to contain all #1 issues, the Carson City collection was amassed by a man who hoarded periodicals from his tobacco and candy store during the '40s and '50s, storing them between newspapers inside two storage sheds. After his passing, his wife sold the contents of the sheds to Mark Wilson and Ernie Gerber in the early '90s. The collection yielded impressive key issues such as Marvel Comics #1, All Select #1, Mystery Men #1, and 1939 New York World's Fair. Some copies exhibit a \"#1\" written on the front cover in pencil.", media="../static/images/pedigrees/carsoncity.jpg")

ped9 = Pedigree(title="Central Valley", description="The origin of the Central Valley collection is unknown. A trucker bought the books in an estate sale in Northern California and flipped them to Brian Peets in 1993, who decided to keep the collection intact for 13 years. Containing nearly 400 comic books, the Central Valley collection exhibits fresh, white copies from the late '30s to the early '50s, including many high grade Superman and Batman titles. Once Peets decided to sell the collection, he had most of them CGC graded. Although some copies exhibit a date stamp, a store stamp or a penciled letter on the cover, the markings are not consistent.", media="../static/images/pedigrees/centralvalley.jpg")

ped10 = Pedigree(title="Chicago", description="One of the oldest recognized pedigrees, the Chicago collection was purchased by Joe Sarno from the original owner in 1974. The most famous part of the collection includes near full runs of early Timely issues in high grade, which ultimately ended up in the hands of George Olshevsky, a well-known Timely historian. Olshevsy eventually sold his collection in 1988; prior to that he had meticulously penned a code number, date, and the condition of the book in the margin of an interior page of every issue, one way to identify a Timely Chicago copy. Many of these copies also have his initials penned on the last page.", media="../static/images/pedigrees/chicago.jpg")

# TODO: continue entering these pedigrees



# Add new messages to session, so they'll persist
db.session.add(ped1)
db.session.add(ped2)
db.session.add(ped3)
db.session.add(ped4)
db.session.add(ped5)
db.session.add(ped6)
db.session.add(ped7)
db.session.add(ped8)
db.session.add(ped9)
db.session.add(ped10)
# db.session.add(ped2)
# db.session.add(ped3)

db.session.commit()
