def CreateExtensionSetting(client, feed_items, campaign_feed, feed_item_ids,
                           platform_restrictions=None):
  campaign_extension_setting_service = client.GetService(
      'CampaignExtensionSettingService', 'v201809')
  extension_feed_items = [{
      CreateSitelinkFeedItem(feed_items, feed_item_id)
  } for feed_item_id in feed_item_ids]
  extension_setting = {
      'extensions': extension_feed_items
  }
  if platform_restrictions:
    extension_setting['platformRestrictions'] = platform_restrictions
  campaign_extension_setting = {
      'campaignId': campaign_feed['campaignId'],
      'extensionType': 'SITELINK',
      'extensionSetting': extension_setting
  }
  operation = {
      'operand': campaign_extension_setting,
      'operator': 'ADD'
  }
  campaign_extension_setting_service.mutate([operation])