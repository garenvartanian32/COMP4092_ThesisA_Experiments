def CreateExtensionSetting(client, feed_items, campaign_feed, feed_item_ids, platform_restrictions=None):
    """Creates the extension setting for a list of Feed Items.

    Args:
        client: an AdWordsClient instance.
        feed_items: the list of all Feed Items.
        campaign_feed: the original Campaign Feed.
        feed_item_ids: the Ids of the feed items for which extension settings should
            be created.
        platform_restrictions: an optional Platform Restriction for the Feed items.
    """
    # Your code here