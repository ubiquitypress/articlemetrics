import TwitterSearch


def twitter_queue():
    'Takes the last used set of twitter credentials and executes the Q until it reaches a count of 160.'
    credentials = models.TwitterCredentials.objects.order_by('last_used')

    search_counter = 0
    cred_counter = 0
    total_cred_counter = credentials.count()

    creds = credentials[0]

    ts = TwitterSearch(
        consumer_key=creds.consumer_key,
        consumer_secret=creds.consumer_secret,
        access_token=creds.access_token,
        access_token_secret=creds.access_token_secret,
    )

    # Once this set has been used for 160 queries, switch to second set of creds.
    if counter >= 160 and cred_counter < total_cred_counter:

        cred_counter += 1
        counter = 0

        try:
            creds = credentials[cred_counter]

            ts = TwitterSearch(
                consumer_key=creds.consumer_key,
                consumer_secret=creds.consumer_secret,
                access_token=creds.access_token,
                access_token_secret=creds.access_token_secret,
            )
        except IndexError:
            exit()
