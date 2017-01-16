# from aqt import mw

# import view

import datetime
start_date = datetime.datetime(2012, 2, 15, 5, 0, 0)#None

def get_date_from_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp / 1000)

def get_day(timestamp):
    date = get_date_from_timestamp(timestamp)
    delta = date - start_date
    return delta.days

anki_crt = get_date_from_timestamp(1352952000*1000) #get_date(mw.col.crt)

def get_date_from_anki_day(anki_day):
    return start_date + datetime.timedelta(days=anki_day)#start_date
    # return datetime.date(2012,02,18) + datetime.timedelta(days=anki_day)#start_date




def repetition_iterator():
    """
    Returns a generator object for iterating through all repetitions
    in chronologically ordered days, and ordered in increasing interval length within each day's repetitions.

    Each iteration yields a tuple: (day, repetitions) where
    day is the number of days since the first day studying with Anki.

    repetitions is a list of tuples: (card_id, interval) where
    -   card_id is the unique card identifier
    -   interval is the number of days the card was moved into the future after the repetition
    """

    import pickle
    with open("hannes_anki_repetitions.pickle") as file:
        hannes_data = pickle.load(file)
    print len(hannes_data)
    for repday in hannes_data:
        # print repday
        yield repday
    return
    # mock_data = [
    #     # [(0, 0),(1,1),(2,2),(3,3)],
    #     [(i,0) for i in range(40)],
    #     [(i,i) for i in range(40)],
    #     [(1,2),(2,3),(3,10)]
    # ]
    #
    # for i, data in enumerate(mock_data):
    #     yield (i, data)
    # return
    rep = mw.col.db.all("select id, cid, ease, ivl from revlog ORDER BY id, ivl ASC")
    global start_date
    start_date = get_date_from_timestamp(rep[0][0])
    start_date = start_date.replace(minute=anki_crt.minute, hour=anki_crt.hour, second=anki_crt.second)
    # s = ""
    # for i in range(5):
    #     s += str(get_date_from_timestamp(rep[i][0])) + "\n"
    # i = 0
    # while get_day(rep[i][0]) == 0:
    #     i += 1
    # s+= ("i: %d" % i)


    seen_cards = {}

    """
    Make a datastructure to store the positions in time of all 8000 cards.
    Go through each day of repetitions.
    For each day, move the repeated cards to their new positions
    and draw the frame (possibly with animated jumps of cards)
    before going to the next day's repetitions
    """

    reps_each_day = [0]
    last_day = 0
    repetitions = []
    for (t, cid, ease, ivl) in rep:
        day = get_day(t)
        # if view.debug_message == "":
        #     view.debug_message = str(day) + ", " + str(get_date_from_timestamp(t)) + ", " + str(anki_crt)
        if day != last_day:
            yield day, repetitions
            repetitions = []
            for i in range(day-last_day-1):
                yield (last_day+1+i, []) # yield days with no repetitions
            last_day = day
        else:
            # for old_cid, old_ivl in list(repetitions):
            #     if old_cid == cid:
            #         repetitions.remove((old_cid, old_ivl))
            #         print "!"
            repetitions.append((cid, ivl))