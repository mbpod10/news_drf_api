from news.models import Article

seed_data = [
    {
        "author": "Ann M. Simmons",
        "title": "Russia And Ukraine",
        "description": "Breakaway Regions in Ukraine Issue Call-Up Orders as Russia Tests Missiles",
        "body": "Leaders of the Russian-led breakaway regions of eastern Ukraine called on all eligible men to take up arms to defend their territory, escalating tensions that could trigger a full-scale war as the government in Kyiv reported that one of its soldiers had been killed by separatist fighters.\r\n\r\nDenis Pushilin, head of the self-proclaimed Donetsk People’s Republic, on Saturday ordered the general mobilization of men aged between 18 and 55 years old, including reservists, telling them to report to enlistment offices.\r\n\r\n“I appeal to all the men of the Republic, who are able to hold weapons in their hands, to stand up for their families, their children, wives, mothers,” Mr. Pushilin said in a televised address. “Together we will achieve the desired and necessary victory for all of us.”",
        "location": "Moscow",
        "publication_date": "2022-02-19",
        "active": True
    },
    {
        "author": "Nick Timiraos",
        "title": "The Fed And March 2020",
        "description": "March 2020: How the Fed Averted Economic Disaster",
        "body": "Get in the boats and go.” As the coronavirus pandemic upended global commerce in March 2020, Fed Chairman Jerome Powell repeatedly invoked the urgent British evacuations from Dunkirk in World War II.\r\n\r\nThis wasn’t the time, he said, to get hung up on the technicalities that central bank economists and lawyers love to chew over. Mr. Powell bluntly directed his colleagues to move as fast as possible. They devised unparalleled emergency-lending backstops to stem an incipient financial panic that threatened to exacerbate the unfolding economic and public-health emergencies.\r\n\r\nOver the week of March 16, markets experienced an enormous shock to what investors refer to as liquidity, a catchall term for the cost of quickly converting an asset into cash.",
        "location": "Washington",
        "publication_date": "2022-02-18",
        "active": True
    },
    {
        "author": "Ann M. Simmons",
        "title": "2022 Winter Olympics",
        "description": "A Disturbing Night of Olympic Figure Skating Exposes the Dark Side of the Rink",
        "body": "After a wrenching night at the Olympics that ended with Russian teenagers in tears and the sport in tatters, figure skating began to sift through the wreckage of what appeared to be a systemic failure of the people who were supposed to be the adults in the rink. \r\n\r\nAll of the sport’s darkest fears—about pushing ever-younger athletes through more grueling training to achieve ever-more dizzying achievements—exploded in one historic night of collective meltdown.\r\n\r\nFifteen-year old Kamila Valieva faltered and slipped under the glare of a doping scandal, only to be confronted by her coach, Eteri Tutberidze, who demanded: “Why did you stop fighting?”\r\n\r\nAnother Russian teen, 17-year-old Alexandra Trusova who finished second, fell apart over failing to win and declared, “I hate this sport!”",
        "location": "Beijing",
        "publication_date": "2022-02-17",
        "active": True
    }
]


def create_seed(data):
    for object in data:
        article = Article.objects.create(**object)
        article.save()
    print("Seed Data Created...")


create_seed(seed_data)
