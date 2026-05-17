def create_extension_setting(client, feed_items, campaign_feed, feed_item_ids, platform_restrictions=None):
    extension_setting_service = client.GetService('ExtensionSettingService', version='v201809')
    ext_settings = []
    for feed_item in feed_items:
        if feed_item.feedItemId not in feed_item_ids:
            continue
        ext_setting = {
            'extensionType': 'Callout',
            'campaignId': campaign_feed['campaignId'],
            'extensionId': feed_item['feedId'],
            'status': 'ENABLED',
            'platformRestrictions': platform_restrictions
        }
        callout_feed_item = client.GetService('FeedItemService', version='v201809').get(feed_item['feedId'])
        callout_feed_item.attributeValues[0].feedAttributeId # get the first value for attribute
        if not callout_feed_item or not callout_feed_item.attributeValues[0].stringValues:
            continue
        callout_text = callout_feed_item.attributeValues[0].stringValues[0]
        callout_extension = {
            'calloutText': callout_text
        }
        ext_setting['extension'] = callout_extension
        ext_settings.append(ext_setting)
        operations = [{'operator': 'ADD', 'operand': ext_setting} for ext_setting in ext_settings]
        result = extension_setting_service.mutate(operations)
        for res in result['value']:
            print('Callout extension setting with ID %d was added.' % res['extensionFeedItemId']) 
