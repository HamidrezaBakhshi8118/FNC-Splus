# فهرست RPCهای سروش پلاس

منبع: باندل رسمی وب‌کلاینت؛ مشخصات و هش در کاتالوگ JSON همراه پکیج ثبت شده‌اند.
۳۷۴ نام زیر constructor و متد صریح async/sync دارند. آزمون encode/decode و چیدمان فیلدها آفلاین است؛ اجرای زندهٔ تمام عملیات ادعا نمی‌شود.

| RPC | متد کلاینت | نوع | شناسهٔ باینری |
|---|---|---|---|
| `invokeAfterMsg` | `invoke_after_msg` | mutation | `cb9f372d` |
| `initConnection` | `init_connection` | mutation | `c1cd5ea9` |
| `invokeWithLayer` | `invoke_with_layer` | mutation | `da9b0d0d` |
| `auth.sendCode` | `auth_send_code` | mutation | `a677244f` |
| `auth.signUp` | `auth_sign_up` | mutation | `80eee427` |
| `auth.signIn` | `auth_sign_in` | mutation | `8d52a951` |
| `auth.logOut` | `auth_log_out` | mutation | `3e72ba19` |
| `auth.resetAuthorizations` | `auth_reset_authorizations` | mutation | `9fab0d1a` |
| `auth.exportAuthorization` | `auth_export_authorization` | mutation | `e5bfffcd` |
| `auth.importAuthorization` | `auth_import_authorization` | mutation | `a57a7dad` |
| `auth.bindTempAuthKey` | `auth_bind_temp_auth_key` | mutation | `cdd42a05` |
| `auth.checkPassword` | `auth_check_password` | mutation | `d18b4d16` |
| `auth.requestPasswordRecovery` | `auth_request_password_recovery` | mutation | `d897bc66` |
| `auth.resendCode` | `auth_resend_code` | mutation | `3ef1a9bf` |
| `auth.cancelCode` | `auth_cancel_code` | mutation | `1f040578` |
| `auth.dropTempAuthKeys` | `auth_drop_temp_auth_keys` | mutation | `8e48a188` |
| `auth.exportLoginToken` | `auth_export_login_token` | mutation | `b7e085fe` |
| `auth.importLoginToken` | `auth_import_login_token` | mutation | `95ac5ce4` |
| `auth.importWebTokenAuthorization` | `auth_import_web_token_authorization` | mutation | `2db873a9` |
| `auth.sendDeleteAccountCode` | `auth_send_delete_account_code` | mutation | `7fb3ddc0` |
| `auth.resendDeleteAccountCode` | `auth_resend_delete_account_code` | mutation | `633a65a0` |
| `auth.deleteAccount` | `auth_delete_account` | mutation | `441a1ec2` |
| `account.registerDevice` | `account_register_device` | mutation | `ec86017a` |
| `account.unregisterDevice` | `account_unregister_device` | mutation | `6a0d3206` |
| `account.updateNotifySettings` | `account_update_notify_settings` | mutation | `84be5b93` |
| `account.getNotifySettings` | `account_get_notify_settings` | read | `12b3ad31` |
| `account.updateProfile` | `account_update_profile` | mutation | `78515775` |
| `account.updateStatus` | `account_update_status` | mutation | `6628562c` |
| `account.getWallPapers` | `account_get_wall_papers` | read | `7967d36` |
| `account.reportPeer` | `account_report_peer` | mutation | `c5ba3d86` |
| `account.checkUsername` | `account_check_username` | read | `2714d86c` |
| `account.updateUsername` | `account_update_username` | mutation | `3e0bdd7c` |
| `account.getPrivacy` | `account_get_privacy` | read | `dadbc950` |
| `account.setPrivacy` | `account_set_privacy` | mutation | `c9f81ce8` |
| `account.getAuthorizations` | `account_get_authorizations` | read | `e320c158` |
| `account.resetAuthorization` | `account_reset_authorization` | mutation | `df77f3bc` |
| `account.getPassword` | `account_get_password` | read | `548a30f5` |
| `account.getPasswordSettings` | `account_get_password_settings` | read | `9cd4eaf9` |
| `account.updatePasswordSettings` | `account_update_password_settings` | mutation | `a59b102f` |
| `account.sendConfirmPhoneCode` | `account_send_confirm_phone_code` | mutation | `1b3faa88` |
| `account.confirmPhone` | `account_confirm_phone` | mutation | `5f2178c3` |
| `account.getTmpPassword` | `account_get_tmp_password` | read | `449e0b51` |
| `account.getWebAuthorizations` | `account_get_web_authorizations` | read | `182e6d6f` |
| `account.resetWebAuthorization` | `account_reset_web_authorization` | mutation | `2d01b9ef` |
| `account.resetWebAuthorizations` | `account_reset_web_authorizations` | mutation | `682d2594` |
| `account.sendVerifyPhoneCode` | `account_send_verify_phone_code` | mutation | `a5a356f9` |
| `account.confirmPasswordEmail` | `account_confirm_password_email` | mutation | `8fdf1920` |
| `account.getContactSignUpNotification` | `account_get_contact_sign_up_notification` | read | `9f07c728` |
| `account.setContactSignUpNotification` | `account_set_contact_sign_up_notification` | mutation | `cff43f61` |
| `account.getNotifyExceptions` | `account_get_notify_exceptions` | read | `53577479` |
| `account.uploadWallPaper` | `account_upload_wall_paper` | mutation | `e39a8f03` |
| `account.getAutoDownloadSettings` | `account_get_auto_download_settings` | read | `56da0b3f` |
| `account.saveAutoDownloadSettings` | `account_save_auto_download_settings` | mutation | `76f36233` |
| `account.setContentSettings` | `account_set_content_settings` | mutation | `b574b16b` |
| `account.getContentSettings` | `account_get_content_settings` | read | `8b9b4dae` |
| `account.getGlobalPrivacySettings` | `account_get_global_privacy_settings` | read | `eb2b4cf6` |
| `account.setGlobalPrivacySettings` | `account_set_global_privacy_settings` | mutation | `1edaaac2` |
| `account.reportProfilePhoto` | `account_report_profile_photo` | mutation | `fa8cc6f5` |
| `account.setAuthorizationTTL` | `account_set_authorization_t_t_l` | mutation | `bf899aa0` |
| `account.changeAuthorizationSettings` | `account_change_authorization_settings` | mutation | `40f48462` |
| `account.updateEmojiStatus` | `account_update_emoji_status` | mutation | `fbd3de6b` |
| `account.getRecentEmojiStatuses` | `account_get_recent_emoji_statuses` | read | `f578105` |
| `account.reorderUsernames` | `account_reorder_usernames` | mutation | `ef500eab` |
| `account.toggleUsername` | `account_toggle_username` | mutation | `58d6b376` |
| `account.updateGender` | `account_update_gender` | mutation | `7374f514` |
| `account.updateUserLocation` | `account_update_user_location` | mutation | `1cf44003` |
| `users.getUsers` | `users_get_users` | read | `d91a548` |
| `users.getFullUser` | `users_get_full_user` | read | `b60f5918` |
| `conference.createConferenceCall` | `conference_create_conference_call` | mutation | `350ba3bd` |
| `conference.resolveConferenceCall` | `conference_resolve_conference_call` | read | `3af930b4` |
| `conference.getConferenceCall` | `conference_get_conference_call` | read | `78ba8198` |
| `conference.joinConferenceCall` | `conference_join_conference_call` | mutation | `2b04c211` |
| `conference.leaveConferenceCall` | `conference_leave_conference_call` | mutation | `e5f83a5e` |
| `conference.discardConferenceCall` | `conference_discard_conference_call` | mutation | `51620842` |
| `conference.removeConferenceParticipant` | `conference_remove_conference_participant` | mutation | `2d3e2518` |
| `conference.banConferenceParticipant` | `conference_ban_conference_participant` | mutation | `799a53fc` |
| `conference.unbanConferenceParticipant` | `conference_unban_conference_participant` | mutation | `add30f09` |
| `conference.getBannedConferenceParticipants` | `conference_get_banned_conference_participants` | read | `7d69c24c` |
| `conference.getActiveConferenceCalls` | `conference_get_active_conference_calls` | read | `c3f93e37` |
| `conference.muteConferenceParticipant` | `conference_mute_conference_participant` | mutation | `d9a6240f` |
| `conference.setConferenceRating` | `conference_set_conference_rating` | mutation | `c695c533` |
| `contacts.getContacts` | `contacts_get_contacts` | read | `5dd69e12` |
| `contacts.importContacts` | `contacts_import_contacts` | mutation | `2c800be5` |
| `contacts.deleteContacts` | `contacts_delete_contacts` | mutation | `96a0e00` |
| `contacts.block` | `contacts_block` | mutation | `2e2e8734` |
| `contacts.unblock` | `contacts_unblock` | mutation | `b550d328` |
| `contacts.getBlocked` | `contacts_get_blocked` | read | `9a868f80` |
| `contacts.search` | `contacts_search` | read | `11f812d8` |
| `contacts.resolveUsername` | `contacts_resolve_username` | read | `f93ccba3` |
| `contacts.getTopPeers` | `contacts_get_top_peers` | read | `973478b6` |
| `contacts.addContact` | `contacts_add_contact` | mutation | `e8f463d0` |
| `contacts.resolvePhone` | `contacts_resolve_phone` | read | `8af94344` |
| `contacts.editCloseFriends` | `contacts_edit_close_friends` | mutation | `ba6705f0` |
| `messages.getMessages` | `messages_get_messages` | read | `63c66506` |
| `messages.getDialogs` | `messages_get_dialogs` | read | `a0f4cb4f` |
| `messages.getHistory` | `messages_get_history` | read | `4423e6c5` |
| `messages.search` | `messages_search` | read | `a0fda762` |
| `messages.readHistory` | `messages_read_history` | mutation | `e306d3a` |
| `messages.deleteHistory` | `messages_delete_history` | mutation | `b08f922a` |
| `messages.deleteMessages` | `messages_delete_messages` | mutation | `e547869b` |
| `messages.receivedMessages` | `messages_received_messages` | mutation | `5a954c0` |
| `messages.setTyping` | `messages_set_typing` | mutation | `58943ee2` |
| `messages.sendMessage` | `messages_send_message` | mutation | `280d096f` |
| `messages.sendMedia` | `messages_send_media` | mutation | `72ccc23d` |
| `messages.forwardMessages` | `messages_forward_messages` | mutation | `c661bbc4` |
| `messages.reportSpam` | `messages_report_spam` | mutation | `cf1592db` |
| `messages.getPeerSettings` | `messages_get_peer_settings` | read | `efd9a6a2` |
| `messages.report` | `messages_report` | mutation | `8953ab4e` |
| `messages.getChats` | `messages_get_chats` | read | `49e9528f` |
| `messages.getFullChat` | `messages_get_full_chat` | read | `aeb00b34` |
| `messages.editChatTitle` | `messages_edit_chat_title` | mutation | `73783ffd` |
| `messages.editChatPhoto` | `messages_edit_chat_photo` | mutation | `35ddd674` |
| `messages.addChatUser` | `messages_add_chat_user` | mutation | `f24753e3` |
| `messages.deleteChatUser` | `messages_delete_chat_user` | mutation | `a2185cab` |
| `messages.createChat` | `messages_create_chat` | mutation | `34a818` |
| `messages.getDhConfig` | `messages_get_dh_config` | read | `26cf8950` |
| `messages.readMessageContents` | `messages_read_message_contents` | mutation | `36a73f77` |
| `messages.getStickers` | `messages_get_stickers` | read | `d5a5d3a1` |
| `messages.getAllStickers` | `messages_get_all_stickers` | read | `b8a0a1a8` |
| `messages.getWebPagePreview` | `messages_get_web_page_preview` | read | `8b68b0cc` |
| `messages.exportChatInvite` | `messages_export_chat_invite` | mutation | `a02ce5d5` |
| `messages.checkChatInvite` | `messages_check_chat_invite` | read | `3eadb1bb` |
| `messages.importChatInvite` | `messages_import_chat_invite` | mutation | `6c50051c` |
| `messages.getStickerSet` | `messages_get_sticker_set` | read | `c8a0ec74` |
| `messages.installStickerSet` | `messages_install_sticker_set` | mutation | `c78fe460` |
| `messages.uninstallStickerSet` | `messages_uninstall_sticker_set` | mutation | `f96e55de` |
| `messages.startBot` | `messages_start_bot` | mutation | `e6df7378` |
| `messages.getMessagesViews` | `messages_get_messages_views` | read | `5784d3e1` |
| `messages.migrateChat` | `messages_migrate_chat` | mutation | `a2875319` |
| `messages.searchGlobal` | `messages_search_global` | read | `4bc6589a` |
| `messages.getDocumentByHash` | `messages_get_document_by_hash` | read | `b1f2061f` |
| `messages.getSavedGifs` | `messages_get_saved_gifs` | read | `5cf09635` |
| `messages.saveGif` | `messages_save_gif` | mutation | `327a30cb` |
| `messages.getInlineBotResults` | `messages_get_inline_bot_results` | read | `514e999d` |
| `messages.sendInlineBotResult` | `messages_send_inline_bot_result` | mutation | `f7bc68ba` |
| `messages.editMessage` | `messages_edit_message` | mutation | `48f71778` |
| `messages.getBotCallbackAnswer` | `messages_get_bot_callback_answer` | read | `9342ca07` |
| `messages.getPeerDialogs` | `messages_get_peer_dialogs` | read | `e470bcfd` |
| `messages.saveDraft` | `messages_save_draft` | mutation | `7ff3b806` |
| `messages.getFeaturedStickers` | `messages_get_featured_stickers` | read | `64780b14` |
| `messages.readFeaturedStickers` | `messages_read_featured_stickers` | mutation | `5b118126` |
| `messages.getRecentStickers` | `messages_get_recent_stickers` | read | `9da9403b` |
| `messages.saveRecentSticker` | `messages_save_recent_sticker` | mutation | `392718f8` |
| `messages.clearRecentStickers` | `messages_clear_recent_stickers` | mutation | `8999602d` |
| `messages.getArchivedStickers` | `messages_get_archived_stickers` | read | `57f17692` |
| `messages.getCommonChats` | `messages_get_common_chats` | read | `e40ca104` |
| `messages.getWebPage` | `messages_get_web_page` | read | `8d9692a3` |
| `messages.toggleDialogPin` | `messages_toggle_dialog_pin` | mutation | `a731e257` |
| `messages.getPinnedDialogs` | `messages_get_pinned_dialogs` | read | `d6b94df2` |
| `messages.uploadMedia` | `messages_upload_media` | mutation | `519bc2b1` |
| `messages.getFavedStickers` | `messages_get_faved_stickers` | read | `4f1aaa9` |
| `messages.faveSticker` | `messages_fave_sticker` | mutation | `b9ffc55b` |
| `messages.getUnreadMentions` | `messages_get_unread_mentions` | read | `f107e790` |
| `messages.readMentions` | `messages_read_mentions` | mutation | `36e5bf4d` |
| `messages.sendMultiMedia` | `messages_send_multi_media` | mutation | `456e8987` |
| `messages.searchStickerSets` | `messages_search_sticker_sets` | read | `35705b8a` |
| `messages.markDialogUnread` | `messages_mark_dialog_unread` | mutation | `c286d98f` |
| `messages.updatePinnedMessage` | `messages_update_pinned_message` | mutation | `d2aaf7ec` |
| `messages.sendVote` | `messages_send_vote` | mutation | `10ea6184` |
| `messages.getPollResults` | `messages_get_poll_results` | read | `73bb643b` |
| `messages.getOnlines` | `messages_get_onlines` | read | `6e2be050` |
| `messages.editChatAbout` | `messages_edit_chat_about` | mutation | `def60797` |
| `messages.editChatDefaultBannedRights` | `messages_edit_chat_default_banned_rights` | mutation | `a5866b41` |
| `messages.getEmojiKeywordsDifference` | `messages_get_emoji_keywords_difference` | read | `1508b6af` |
| `messages.requestUrlAuth` | `messages_request_url_auth` | mutation | `198fb446` |
| `messages.acceptUrlAuth` | `messages_accept_url_auth` | mutation | `b12c7125` |
| `messages.hidePeerSettingsBar` | `messages_hide_peer_settings_bar` | mutation | `4facb138` |
| `messages.getScheduledHistory` | `messages_get_scheduled_history` | read | `f516760b` |
| `messages.sendScheduledMessages` | `messages_send_scheduled_messages` | mutation | `bd38850a` |
| `messages.deleteScheduledMessages` | `messages_delete_scheduled_messages` | mutation | `59ae2b16` |
| `messages.getPollVotes` | `messages_get_poll_votes` | read | `b86e380e` |
| `messages.getDialogFilters` | `messages_get_dialog_filters` | read | `efd48c89` |
| `messages.getSuggestedDialogFilters` | `messages_get_suggested_dialog_filters` | read | `a29cd42c` |
| `messages.updateDialogFilter` | `messages_update_dialog_filter` | mutation | `1ad4a04a` |
| `messages.updateDialogFiltersOrder` | `messages_update_dialog_filters_order` | mutation | `c563c1e4` |
| `messages.getReplies` | `messages_get_replies` | read | `22ddd30c` |
| `messages.getDiscussionMessage` | `messages_get_discussion_message` | read | `446972fd` |
| `messages.readDiscussion` | `messages_read_discussion` | mutation | `f731a9f4` |
| `messages.unpinAllMessages` | `messages_unpin_all_messages` | mutation | `ee22b9a8` |
| `messages.deleteChat` | `messages_delete_chat` | mutation | `5bd0ee50` |
| `messages.getExportedChatInvites` | `messages_get_exported_chat_invites` | read | `a2b5a3f6` |
| `messages.editExportedChatInvite` | `messages_edit_exported_chat_invite` | mutation | `bdca2f75` |
| `messages.deleteRevokedExportedChatInvites` | `messages_delete_revoked_exported_chat_invites` | mutation | `56987bd5` |
| `messages.deleteExportedChatInvite` | `messages_delete_exported_chat_invite` | mutation | `d464a42b` |
| `messages.getChatInviteImporters` | `messages_get_chat_invite_importers` | read | `df04dd4e` |
| `messages.getMessageReadParticipants` | `messages_get_message_read_participants` | read | `31c1c44f` |
| `messages.hideChatJoinRequest` | `messages_hide_chat_join_request` | mutation | `7fe7e815` |
| `messages.hideAllChatJoinRequests` | `messages_hide_all_chat_join_requests` | mutation | `e085f4ea` |
| `messages.toggleNoForwards` | `messages_toggle_no_forwards` | mutation | `b11eafa2` |
| `messages.saveDefaultSendAs` | `messages_save_default_send_as` | mutation | `ccfddf96` |
| `messages.sendReaction` | `messages_send_reaction` | mutation | `d30d78d4` |
| `messages.getMessagesReactions` | `messages_get_messages_reactions` | read | `8bba90e6` |
| `messages.getMessageReactionsList` | `messages_get_message_reactions_list` | read | `461b3f48` |
| `messages.setChatAvailableReactions` | `messages_set_chat_available_reactions` | mutation | `feb16771` |
| `messages.getAvailableReactions` | `messages_get_available_reactions` | read | `18dea0ac` |
| `messages.setDefaultReaction` | `messages_set_default_reaction` | mutation | `4f47a016` |
| `messages.translateText` | `messages_translate_text` | mutation | `63183030` |
| `messages.getUnreadReactions` | `messages_get_unread_reactions` | read | `3223495b` |
| `messages.readReactions` | `messages_read_reactions` | mutation | `54aa7f8e` |
| `messages.getAttachMenuBots` | `messages_get_attach_menu_bots` | read | `16fcc2cb` |
| `messages.getAttachMenuBot` | `messages_get_attach_menu_bot` | read | `77216192` |
| `messages.toggleBotInAttachMenu` | `messages_toggle_bot_in_attach_menu` | mutation | `69f59d69` |
| `messages.requestWebView` | `messages_request_web_view` | mutation | `269dc2c1` |
| `messages.prolongWebView` | `messages_prolong_web_view` | mutation | `b0d81a83` |
| `messages.requestSimpleWebView` | `messages_request_simple_web_view` | mutation | `1a46500a` |
| `messages.sendWebViewResultMessage` | `messages_send_web_view_result_message` | mutation | `a4314f5` |
| `messages.sendWebViewData` | `messages_send_web_view_data` | mutation | `dc0242c8` |
| `messages.transcribeAudio` | `messages_transcribe_audio` | mutation | `269e9a49` |
| `messages.getCustomEmojiDocuments` | `messages_get_custom_emoji_documents` | read | `d9ab0f54` |
| `messages.getEmojiStickers` | `messages_get_emoji_stickers` | read | `fbfca18f` |
| `messages.getFeaturedEmojiStickers` | `messages_get_featured_emoji_stickers` | read | `ecf6736` |
| `messages.getTopReactions` | `messages_get_top_reactions` | read | `bb8125ba` |
| `messages.getRecentReactions` | `messages_get_recent_reactions` | read | `39461db2` |
| `messages.clearRecentReactions` | `messages_clear_recent_reactions` | mutation | `9dfeefb4` |
| `messages.getExtendedMedia` | `messages_get_extended_media` | read | `84f80814` |
| `messages.togglePeerTranslations` | `messages_toggle_peer_translations` | mutation | `e47cb579` |
| `messages.getBotApp` | `messages_get_bot_app` | read | `34fdc5c3` |
| `messages.requestAppWebView` | `messages_request_app_web_view` | mutation | `8c5a3b3c` |
| `updates.getState` | `updates_get_state` | read | `edd4882a` |
| `updates.getDifference` | `updates_get_difference` | read | `19c2f763` |
| `updates.getChannelDifference` | `updates_get_channel_difference` | read | `3173d78` |
| `photos.updateProfilePhoto` | `photos_update_profile_photo` | mutation | `9e82039` |
| `photos.uploadProfilePhoto` | `photos_upload_profile_photo` | mutation | `388a3b5` |
| `photos.deletePhotos` | `photos_delete_photos` | mutation | `87cf7f2f` |
| `photos.getUserPhotos` | `photos_get_user_photos` | read | `91cd32a8` |
| `photos.uploadContactProfilePhoto` | `photos_upload_contact_profile_photo` | mutation | `e14c4a71` |
| `upload.saveFilePart` | `upload_save_file_part` | mutation | `b304a621` |
| `upload.getFile` | `upload_get_file` | read | `be5335be` |
| `upload.saveBigFilePart` | `upload_save_big_file_part` | mutation | `de7b673d` |
| `upload.getWebFile` | `upload_get_web_file` | read | `24e6818d` |
| `help.getConfig` | `help_get_config` | read | `c4f9186b` |
| `help.getNearestDc` | `help_get_nearest_dc` | read | `1fb33026` |
| `help.getSupport` | `help_get_support` | read | `9cdf08cd` |
| `help.acceptTermsOfService` | `help_accept_terms_of_service` | mutation | `ee72f79a` |
| `help.getAppConfig` | `help_get_app_config` | read | `61e3f854` |
| `help.getCountriesList` | `help_get_countries_list` | read | `735787a8` |
| `help.getPremiumPromo` | `help_get_premium_promo` | read | `b81b93d4` |
| `help.getPeerColors` | `help_get_peer_colors` | read | `da80f42f` |
| `help.getPeerProfileColors` | `help_get_peer_profile_colors` | read | `abcfa9fd` |
| `channels.readHistory` | `channels_read_history` | mutation | `cc104937` |
| `channels.deleteMessages` | `channels_delete_messages` | mutation | `84c1fd4e` |
| `channels.getMessages` | `channels_get_messages` | read | `ad8c9a23` |
| `channels.getParticipants` | `channels_get_participants` | read | `77ced9d0` |
| `channels.getParticipant` | `channels_get_participant` | read | `a0ab6cc6` |
| `channels.getChannels` | `channels_get_channels` | read | `a7f6bbb` |
| `channels.getFullChannel` | `channels_get_full_channel` | read | `8736a09` |
| `channels.createChannel` | `channels_create_channel` | mutation | `91006707` |
| `channels.editAdmin` | `channels_edit_admin` | mutation | `d33c8902` |
| `channels.editTitle` | `channels_edit_title` | mutation | `566decd0` |
| `channels.editPhoto` | `channels_edit_photo` | mutation | `f12e57c9` |
| `channels.checkUsername` | `channels_check_username` | read | `10e6bd2c` |
| `channels.updateUsername` | `channels_update_username` | mutation | `3514b3de` |
| `channels.joinChannel` | `channels_join_channel` | mutation | `24b524c5` |
| `channels.leaveChannel` | `channels_leave_channel` | mutation | `f836aa95` |
| `channels.inviteToChannel` | `channels_invite_to_channel` | mutation | `199f3a6c` |
| `channels.deleteChannel` | `channels_delete_channel` | mutation | `c0111fe3` |
| `channels.toggleSignatures` | `channels_toggle_signatures` | mutation | `1f69b606` |
| `channels.getAdminedPublicChannels` | `channels_get_admined_public_channels` | read | `f8b036af` |
| `channels.editBanned` | `channels_edit_banned` | mutation | `96e6cd81` |
| `channels.readMessageContents` | `channels_read_message_contents` | mutation | `eab5dc38` |
| `channels.togglePreHistoryHidden` | `channels_toggle_pre_history_hidden` | mutation | `eabbb94c` |
| `channels.getGroupsForDiscussion` | `channels_get_groups_for_discussion` | read | `f5dad378` |
| `channels.setDiscussionGroup` | `channels_set_discussion_group` | mutation | `40582bb2` |
| `channels.viewSponsoredMessage` | `channels_view_sponsored_message` | mutation | `beaedb94` |
| `channels.getSponsoredMessages` | `channels_get_sponsored_messages` | read | `ec210fbf` |
| `channels.getSendAs` | `channels_get_send_as` | read | `dc770ee` |
| `channels.toggleJoinToSend` | `channels_toggle_join_to_send` | mutation | `e4cb9580` |
| `channels.toggleJoinRequest` | `channels_toggle_join_request` | mutation | `4c2985b6` |
| `channels.reorderUsernames` | `channels_reorder_usernames` | mutation | `b45ced1d` |
| `channels.toggleUsername` | `channels_toggle_username` | mutation | `50f24105` |
| `channels.deactivateAllUsernames` | `channels_deactivate_all_usernames` | mutation | `a245dd3` |
| `channels.toggleForum` | `channels_toggle_forum` | mutation | `a4298b29` |
| `channels.createForumTopic` | `channels_create_forum_topic` | mutation | `f40c0224` |
| `channels.getForumTopics` | `channels_get_forum_topics` | read | `de560d1` |
| `channels.getForumTopicsByID` | `channels_get_forum_topics_by_i_d` | read | `b0831eb9` |
| `channels.editForumTopic` | `channels_edit_forum_topic` | mutation | `f4dfa185` |
| `channels.updatePinnedForumTopic` | `channels_update_pinned_forum_topic` | mutation | `6c2d9026` |
| `channels.deleteTopicHistory` | `channels_delete_topic_history` | mutation | `34435f2d` |
| `channels.toggleParticipantsHidden` | `channels_toggle_participants_hidden` | mutation | `6a6e7854` |
| `channels.clickSponsoredMessage` | `channels_click_sponsored_message` | mutation | `18afbc93` |
| `channels.toggleViewForumAsMessages` | `channels_toggle_view_forum_as_messages` | mutation | `9738bb15` |
| `channels.toggleMembershipMessageVisibility` | `channels_toggle_membership_message_visibility` | mutation | `75646c0` |
| `bots.canSendMessage` | `bots_can_send_message` | mutation | `1359f4e6` |
| `bots.allowSendMessage` | `bots_allow_send_message` | mutation | `f132e3ef` |
| `bots.invokeWebViewCustomMethod` | `bots_invoke_web_view_custom_method` | mutation | `87fc5e7` |
| `payments.getPaymentForm` | `payments_get_payment_form` | read | `37148dbb` |
| `payments.getPaymentReceipt` | `payments_get_payment_receipt` | read | `2478d1cc` |
| `payments.validateRequestedInfo` | `payments_validate_requested_info` | mutation | `b6c8f12b` |
| `payments.sendPaymentForm` | `payments_send_payment_form` | mutation | `2d03522f` |
| `payments.getSavedInfo` | `payments_get_saved_info` | read | `227d824b` |
| `payments.checkGiftCode` | `payments_check_gift_code` | read | `8e51b4c1` |
| `payments.applyGiftCode` | `payments_apply_gift_code` | mutation | `f6e26854` |
| `payments.getGiveawayInfo` | `payments_get_giveaway_info` | read | `f4239425` |
| `phone.requestCall` | `phone_request_call` | mutation | `42ff96ed` |
| `phone.acceptCall` | `phone_accept_call` | mutation | `3bd2b4a0` |
| `phone.confirmCall` | `phone_confirm_call` | mutation | `2efe1722` |
| `phone.receivedCall` | `phone_received_call` | mutation | `17d54f61` |
| `phone.discardCall` | `phone_discard_call` | mutation | `b2cbc1c0` |
| `phone.setCallRating` | `phone_set_call_rating` | mutation | `59ead627` |
| `phone.saveCallDebug` | `phone_save_call_debug` | mutation | `277add7e` |
| `phone.sendSignalingData` | `phone_send_signaling_data` | mutation | `ff7a9383` |
| `phone.createGroupCall` | `phone_create_group_call` | mutation | `48cdc6d8` |
| `phone.joinGroupCall` | `phone_join_group_call` | mutation | `b132ff7b` |
| `phone.leaveGroupCall` | `phone_leave_group_call` | mutation | `500377f9` |
| `phone.discardGroupCall` | `phone_discard_group_call` | mutation | `7a777135` |
| `phone.getGroupCall` | `phone_get_group_call` | read | `41845db` |
| `phone.getGroupParticipants` | `phone_get_group_participants` | read | `c558d8ab` |
| `phone.editGroupCallParticipant` | `phone_edit_group_call_participant` | mutation | `a5273abf` |
| `phone.exportGroupCallInvite` | `phone_export_group_call_invite` | mutation | `e6aa647f` |
| `phone.toggleGroupCallStartSubscription` | `phone_toggle_group_call_start_subscription` | mutation | `219c34e6` |
| `phone.joinGroupCallPresentation` | `phone_join_group_call_presentation` | mutation | `cbea6bc4` |
| `phone.leaveGroupCallPresentation` | `phone_leave_group_call_presentation` | mutation | `1c50d144` |
| `langpack.getLangPack` | `langpack_get_lang_pack` | read | `f2f2330a` |
| `langpack.getStrings` | `langpack_get_strings` | read | `efea3803` |
| `langpack.getDifference` | `langpack_get_difference` | read | `cd984aa5` |
| `langpack.getLanguages` | `langpack_get_languages` | read | `42c6978f` |
| `folders.editPeerFolders` | `folders_edit_peer_folders` | mutation | `6847d0ab` |
| `stats.getBroadcastStats` | `stats_get_broadcast_stats` | read | `ab42441a` |
| `stats.loadAsyncGraph` | `stats_load_async_graph` | mutation | `621d5fa0` |
| `stats.getMegagroupStats` | `stats_get_megagroup_stats` | read | `dcdf8607` |
| `stats.getMessagePublicForwards` | `stats_get_message_public_forwards` | read | `5630281b` |
| `stats.getMessageStats` | `stats_get_message_stats` | read | `b6e0a3f5` |
| `stats.getStoryStats` | `stats_get_story_stats` | read | `374fef40` |
| `stats.getStoryPublicForwards` | `stats_get_story_public_forwards` | read | `a6437ef6` |
| `chatlists.exportChatlistInvite` | `chatlists_export_chatlist_invite` | mutation | `8472478e` |
| `chatlists.deleteExportedInvite` | `chatlists_delete_exported_invite` | mutation | `719c5c5e` |
| `chatlists.editExportedInvite` | `chatlists_edit_exported_invite` | mutation | `653db63d` |
| `chatlists.getExportedInvites` | `chatlists_get_exported_invites` | read | `ce03da83` |
| `chatlists.checkChatlistInvite` | `chatlists_check_chatlist_invite` | read | `41c10fff` |
| `chatlists.joinChatlistInvite` | `chatlists_join_chatlist_invite` | mutation | `a6b1e39a` |
| `chatlists.getLeaveChatlistSuggestions` | `chatlists_get_leave_chatlist_suggestions` | read | `fdbcd714` |
| `chatlists.leaveChatlist` | `chatlists_leave_chatlist` | mutation | `74fae13a` |
| `stories.editStory` | `stories_edit_story` | mutation | `b583ba46` |
| `stories.deleteStories` | `stories_delete_stories` | mutation | `ae59db5f` |
| `stories.togglePinned` | `stories_toggle_pinned` | mutation | `9a75a1ef` |
| `stories.getAllStories` | `stories_get_all_stories` | read | `eeb0d625` |
| `stories.getPinnedStories` | `stories_get_pinned_stories` | read | `5821a5dc` |
| `stories.getStoriesArchive` | `stories_get_stories_archive` | read | `b4352016` |
| `stories.getStoriesByID` | `stories_get_stories_by_i_d` | read | `5774ca74` |
| `stories.readStories` | `stories_read_stories` | mutation | `a556dac8` |
| `stories.incrementStoryViews` | `stories_increment_story_views` | mutation | `b2028afb` |
| `stories.getStoryViewsList` | `stories_get_story_views_list` | read | `7ed23c57` |
| `stories.exportStoryLink` | `stories_export_story_link` | mutation | `7b8def20` |
| `stories.report` | `stories_report` | mutation | `1923fa8c` |
| `stories.activateStealthMode` | `stories_activate_stealth_mode` | mutation | `57bbd166` |
| `stories.sendReaction` | `stories_send_reaction` | mutation | `7fd736b2` |
| `stories.getPeerStories` | `stories_get_peer_stories` | read | `2c4ada50` |
| `stories.getPeerMaxIDs` | `stories_get_peer_max_i_ds` | read | `535983c3` |
| `stories.togglePeerStoriesHidden` | `stories_toggle_peer_stories_hidden` | mutation | `bd0415c4` |
| `premium.getBoostsList` | `premium_get_boosts_list` | read | `60f67660` |
| `premium.getMyBoosts` | `premium_get_my_boosts` | read | `be77b4a` |
| `premium.applyBoost` | `premium_apply_boost` | mutation | `6b7da746` |
| `premium.getBoostsStatus` | `premium_get_boosts_status` | read | `42f1f61` |
| `thirdParty.request` | `third_party_request` | mutation | `c8520739` |
| `thirdParty.tell` | `third_party_tell` | mutation | `a7ebdf75` |
| `help.getTimezonesList` | `help_get_timezones_list` | read | `49b30240` |
| `account.updateBusinessWorkHours` | `account_update_business_work_hours` | mutation | `4b00e066` |
| `account.updateBirthday` | `account_update_birthday` | mutation | `cc6e0c11` |
| `contacts.getBirthdays` | `contacts_get_birthdays` | read | `daeda864` |
| `account.saveMusic` | `account_save_music` | mutation | `b26732a9` |
| `account.setMainProfileTab` | `account_set_main_profile_tab` | mutation | `5dee78b0` |
| `account.getSavedMusicIds` | `account_get_saved_music_ids` | read | `e09d5faf` |
| `account.updatePersonalChannel` | `account_update_personal_channel` | mutation | `d94305e0` |
| `users.getSavedMusic` | `users_get_saved_music` | read | `788d7fe3` |
| `users.getSavedMusicByID` | `users_get_saved_music_by_i_d` | read | `7573a4e9` |
| `messages.toggleDialogFilterTags` | `messages_toggle_dialog_filter_tags` | mutation | `fd2dda49` |
| `req_pq` | `req_pq` | mutation | `60469778` |
| `req_pq_multi` | `req_pq_multi` | mutation | `be7e8ef1` |
| `req_pq_multi_new` | `req_pq_multi_new` | mutation | `51b410fd` |
| `req_DH_params` | `req__d_h_params` | mutation | `d712e4be` |
| `set_client_DH_params` | `set_client__d_h_params` | mutation | `f5045f1f` |
| `destroy_auth_key` | `destroy_auth_key` | mutation | `d1435160` |
| `ping` | `ping` | read | `7abe77ec` |
| `ping_delay_disconnect` | `ping_delay_disconnect` | read | `f3427b8c` |

## تعریف‌های ورودی رسمی

این بلوک‌ها قرارداد wire هستند؛ مقدارهای `flags` توسط سازندهٔ درخواست مدیریت می‌شوند.

### `invokeAfterMsg`

```tl
invokeAfterMsg#cb9f372d {X:Type} msg_id:long query:!X = X;
```

### `initConnection`

```tl
initConnection#c1cd5ea9 {X:Type} flags:# api_id:int device_model:string system_version:string app_version:string system_lang_code:string lang_pack:string lang_code:string proxy:flags.0?InputClientProxy params:flags.1?JSONValue query:!X = X;
```

### `invokeWithLayer`

```tl
invokeWithLayer#da9b0d0d {X:Type} layer:int query:!X = X;
```

### `auth.sendCode`

```tl
auth.sendCode#a677244f phone_number:string api_id:int api_hash:string settings:CodeSettings = auth.SentCode;
```

### `auth.signUp`

```tl
auth.signUp#80eee427 phone_number:string phone_code_hash:string first_name:string last_name:string = auth.Authorization;
```

### `auth.signIn`

```tl
auth.signIn#8d52a951 flags:# phone_number:string phone_code_hash:string phone_code:flags.0?string email_verification:flags.1?EmailVerification = auth.Authorization;
```

### `auth.logOut`

```tl
auth.logOut#3e72ba19 = auth.LoggedOut;
```

### `auth.resetAuthorizations`

```tl
auth.resetAuthorizations#9fab0d1a = Bool;
```

### `auth.exportAuthorization`

```tl
auth.exportAuthorization#e5bfffcd dc_id:int = auth.ExportedAuthorization;
```

### `auth.importAuthorization`

```tl
auth.importAuthorization#a57a7dad id:long bytes:bytes = auth.Authorization;
```

### `auth.bindTempAuthKey`

```tl
auth.bindTempAuthKey#cdd42a05 perm_auth_key_id:long nonce:long expires_at:int encrypted_message:bytes = Bool;
```

### `auth.checkPassword`

```tl
auth.checkPassword#d18b4d16 password:InputCheckPasswordSRP = auth.Authorization;
```

### `auth.requestPasswordRecovery`

```tl
auth.requestPasswordRecovery#d897bc66 = auth.PasswordRecovery;
```

### `auth.resendCode`

```tl
auth.resendCode#3ef1a9bf phone_number:string phone_code_hash:string = auth.SentCode;
```

### `auth.cancelCode`

```tl
auth.cancelCode#1f040578 phone_number:string phone_code_hash:string = Bool;
```

### `auth.dropTempAuthKeys`

```tl
auth.dropTempAuthKeys#8e48a188 except_auth_keys:Vector<long> = Bool;
```

### `auth.exportLoginToken`

```tl
auth.exportLoginToken#b7e085fe api_id:int api_hash:string except_ids:Vector<long> = auth.LoginToken;
```

### `auth.importLoginToken`

```tl
auth.importLoginToken#95ac5ce4 token:bytes = auth.LoginToken;
```

### `auth.importWebTokenAuthorization`

```tl
auth.importWebTokenAuthorization#2db873a9 api_id:int api_hash:string web_auth_token:string = auth.Authorization;
```

### `auth.sendDeleteAccountCode`

```tl
auth.sendDeleteAccountCode#7fb3ddc0 = auth.sentDeleteAccountCode;
```

### `auth.resendDeleteAccountCode`

```tl
auth.resendDeleteAccountCode#633a65a0 = auth.sentDeleteAccountCode;
```

### `auth.deleteAccount`

```tl
auth.deleteAccount#441a1ec2 delete_account_code:string = Bool;
```

### `account.registerDevice`

```tl
account.registerDevice#ec86017a flags:# no_muted:flags.0?true token_type:int token:string app_sandbox:Bool secret:bytes other_uids:Vector<long> = Bool;
```

### `account.unregisterDevice`

```tl
account.unregisterDevice#6a0d3206 token_type:int token:string other_uids:Vector<long> = Bool;
```

### `account.updateNotifySettings`

```tl
account.updateNotifySettings#84be5b93 peer:InputNotifyPeer settings:InputPeerNotifySettings = Bool;
```

### `account.getNotifySettings`

```tl
account.getNotifySettings#12b3ad31 peer:InputNotifyPeer = PeerNotifySettings;
```

### `account.updateProfile`

```tl
account.updateProfile#78515775 flags:# first_name:flags.0?string last_name:flags.1?string about:flags.2?string = User;
```

### `account.updateStatus`

```tl
account.updateStatus#6628562c offline:Bool = Bool;
```

### `account.getWallPapers`

```tl
account.getWallPapers#7967d36 hash:long = account.WallPapers;
```

### `account.reportPeer`

```tl
account.reportPeer#c5ba3d86 peer:InputPeer reason:ReportReason message:string = Bool;
```

### `account.checkUsername`

```tl
account.checkUsername#2714d86c username:string = Bool;
```

### `account.updateUsername`

```tl
account.updateUsername#3e0bdd7c username:string = User;
```

### `account.getPrivacy`

```tl
account.getPrivacy#dadbc950 key:InputPrivacyKey = account.PrivacyRules;
```

### `account.setPrivacy`

```tl
account.setPrivacy#c9f81ce8 key:InputPrivacyKey rules:Vector<InputPrivacyRule> = account.PrivacyRules;
```

### `account.getAuthorizations`

```tl
account.getAuthorizations#e320c158 = account.Authorizations;
```

### `account.resetAuthorization`

```tl
account.resetAuthorization#df77f3bc hash:long = Bool;
```

### `account.getPassword`

```tl
account.getPassword#548a30f5 = account.Password;
```

### `account.getPasswordSettings`

```tl
account.getPasswordSettings#9cd4eaf9 password:InputCheckPasswordSRP = account.PasswordSettings;
```

### `account.updatePasswordSettings`

```tl
account.updatePasswordSettings#a59b102f password:InputCheckPasswordSRP new_settings:account.PasswordInputSettings = Bool;
```

### `account.sendConfirmPhoneCode`

```tl
account.sendConfirmPhoneCode#1b3faa88 hash:string settings:CodeSettings = auth.SentCode;
```

### `account.confirmPhone`

```tl
account.confirmPhone#5f2178c3 phone_code_hash:string phone_code:string = Bool;
```

### `account.getTmpPassword`

```tl
account.getTmpPassword#449e0b51 password:InputCheckPasswordSRP period:int = account.TmpPassword;
```

### `account.getWebAuthorizations`

```tl
account.getWebAuthorizations#182e6d6f = account.WebAuthorizations;
```

### `account.resetWebAuthorization`

```tl
account.resetWebAuthorization#2d01b9ef hash:long = Bool;
```

### `account.resetWebAuthorizations`

```tl
account.resetWebAuthorizations#682d2594 = Bool;
```

### `account.sendVerifyPhoneCode`

```tl
account.sendVerifyPhoneCode#a5a356f9 phone_number:string settings:CodeSettings = auth.SentCode;
```

### `account.confirmPasswordEmail`

```tl
account.confirmPasswordEmail#8fdf1920 code:string = Bool;
```

### `account.getContactSignUpNotification`

```tl
account.getContactSignUpNotification#9f07c728 = Bool;
```

### `account.setContactSignUpNotification`

```tl
account.setContactSignUpNotification#cff43f61 silent:Bool = Bool;
```

### `account.getNotifyExceptions`

```tl
account.getNotifyExceptions#53577479 flags:# compare_sound:flags.1?true compare_stories:flags.2?true peer:flags.0?InputNotifyPeer = Updates;
```

### `account.uploadWallPaper`

```tl
account.uploadWallPaper#e39a8f03 flags:# for_chat:flags.0?true file:InputFile mime_type:string settings:WallPaperSettings = WallPaper;
```

### `account.getAutoDownloadSettings`

```tl
account.getAutoDownloadSettings#56da0b3f = account.AutoDownloadSettings;
```

### `account.saveAutoDownloadSettings`

```tl
account.saveAutoDownloadSettings#76f36233 flags:# low:flags.0?true high:flags.1?true settings:AutoDownloadSettings = Bool;
```

### `account.setContentSettings`

```tl
account.setContentSettings#b574b16b flags:# sensitive_enabled:flags.0?true = Bool;
```

### `account.getContentSettings`

```tl
account.getContentSettings#8b9b4dae = account.ContentSettings;
```

### `account.getGlobalPrivacySettings`

```tl
account.getGlobalPrivacySettings#eb2b4cf6 = GlobalPrivacySettings;
```

### `account.setGlobalPrivacySettings`

```tl
account.setGlobalPrivacySettings#1edaaac2 settings:GlobalPrivacySettings = GlobalPrivacySettings;
```

### `account.reportProfilePhoto`

```tl
account.reportProfilePhoto#fa8cc6f5 peer:InputPeer photo_id:InputPhoto reason:ReportReason message:string = Bool;
```

### `account.setAuthorizationTTL`

```tl
account.setAuthorizationTTL#bf899aa0 authorization_ttl_days:int = Bool;
```

### `account.changeAuthorizationSettings`

```tl
account.changeAuthorizationSettings#40f48462 flags:# confirmed:flags.3?true hash:long encrypted_requests_disabled:flags.0?Bool call_requests_disabled:flags.1?Bool = Bool;
```

### `account.updateEmojiStatus`

```tl
account.updateEmojiStatus#fbd3de6b emoji_status:EmojiStatus = Bool;
```

### `account.getRecentEmojiStatuses`

```tl
account.getRecentEmojiStatuses#f578105 hash:long = account.EmojiStatuses;
```

### `account.reorderUsernames`

```tl
account.reorderUsernames#ef500eab order:Vector<string> = Bool;
```

### `account.toggleUsername`

```tl
account.toggleUsername#58d6b376 username:string active:Bool = Bool;
```

### `account.updateGender`

```tl
account.updateGender#7374f514 flags:# gender:flags.0?Gender = Bool;
```

### `account.updateUserLocation`

```tl
account.updateUserLocation#1cf44003 flags:# geo_point:flags.0?InputGeoPoint = Bool;
```

### `users.getUsers`

```tl
users.getUsers#d91a548 id:Vector<InputUser> = Vector<User>;
```

### `users.getFullUser`

```tl
users.getFullUser#b60f5918 id:InputUser = users.UserFull;
```

### `conference.createConferenceCall`

```tl
conference.createConferenceCall#350ba3bd flags:# version:string random_id:long name:flags.0?string = ConferenceCreated;
```

### `conference.resolveConferenceCall`

```tl
conference.resolveConferenceCall#3af930b4 slug:string = conference.ConferenceCall;
```

### `conference.getConferenceCall`

```tl
conference.getConferenceCall#78ba8198 conference:InputConferenceCall = conference.ConferenceCall;
```

### `conference.joinConferenceCall`

```tl
conference.joinConferenceCall#2b04c211 version:string conference:InputConferenceCall = Updates;
```

### `conference.leaveConferenceCall`

```tl
conference.leaveConferenceCall#e5f83a5e conference:InputConferenceCall = Bool;
```

### `conference.discardConferenceCall`

```tl
conference.discardConferenceCall#51620842 conference:InputConferenceCall = Bool;
```

### `conference.removeConferenceParticipant`

```tl
conference.removeConferenceParticipant#2d3e2518 conference:InputConferenceCall participant:InputConferenceParticipant = Bool;
```

### `conference.banConferenceParticipant`

```tl
conference.banConferenceParticipant#799a53fc conference:InputConferenceCall peer:InputPeer = Bool;
```

### `conference.unbanConferenceParticipant`

```tl
conference.unbanConferenceParticipant#add30f09 conference:InputConferenceCall peer:InputPeer = Bool;
```

### `conference.getBannedConferenceParticipants`

```tl
conference.getBannedConferenceParticipants#7d69c24c conference:InputConferenceCall = BannedConferenceParticipants;
```

### `conference.getActiveConferenceCalls`

```tl
conference.getActiveConferenceCalls#c3f93e37 flags:# limit:int offset:flags.0?string = ActiveConferenceCalls;
```

### `conference.muteConferenceParticipant`

```tl
conference.muteConferenceParticipant#d9a6240f conference:InputConferenceCall participant:InputConferenceParticipant track:InputConferenceMediaTrack = Bool;
```

### `conference.setConferenceRating`

```tl
conference.setConferenceRating#c695c533 conference:InputConferenceCall rating:int comment:string = Updates;
```

### `contacts.getContacts`

```tl
contacts.getContacts#5dd69e12 hash:long = contacts.Contacts;
```

### `contacts.importContacts`

```tl
contacts.importContacts#2c800be5 contacts:Vector<InputContact> = contacts.ImportedContacts;
```

### `contacts.deleteContacts`

```tl
contacts.deleteContacts#96a0e00 id:Vector<InputUser> = Updates;
```

### `contacts.block`

```tl
contacts.block#2e2e8734 flags:# my_stories_from:flags.0?true id:InputPeer = Bool;
```

### `contacts.unblock`

```tl
contacts.unblock#b550d328 flags:# my_stories_from:flags.0?true id:InputPeer = Bool;
```

### `contacts.getBlocked`

```tl
contacts.getBlocked#9a868f80 flags:# my_stories_from:flags.0?true offset:int limit:int = contacts.Blocked;
```

### `contacts.search`

```tl
contacts.search#11f812d8 q:string limit:int = contacts.Found;
```

### `contacts.resolveUsername`

```tl
contacts.resolveUsername#f93ccba3 username:string = contacts.ResolvedPeer;
```

### `contacts.getTopPeers`

```tl
contacts.getTopPeers#973478b6 flags:# correspondents:flags.0?true bots_pm:flags.1?true bots_inline:flags.2?true phone_calls:flags.3?true forward_users:flags.4?true forward_chats:flags.5?true groups:flags.10?true channels:flags.15?true offset:int limit:int hash:long = contacts.TopPeers;
```

### `contacts.addContact`

```tl
contacts.addContact#e8f463d0 flags:# add_phone_privacy_exception:flags.0?true id:InputUser first_name:string last_name:string phone:string = Updates;
```

### `contacts.resolvePhone`

```tl
contacts.resolvePhone#8af94344 phone:string = contacts.ResolvedPeer;
```

### `contacts.editCloseFriends`

```tl
contacts.editCloseFriends#ba6705f0 id:Vector<long> = Bool;
```

### `messages.getMessages`

```tl
messages.getMessages#63c66506 id:Vector<InputMessage> = messages.Messages;
```

### `messages.getDialogs`

```tl
messages.getDialogs#a0f4cb4f flags:# exclude_pinned:flags.0?true folder_id:flags.1?int offset_date:int offset_id:int offset_peer:InputPeer limit:int hash:long = messages.Dialogs;
```

### `messages.getHistory`

```tl
messages.getHistory#4423e6c5 peer:InputPeer offset_id:int offset_date:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages;
```

### `messages.search`

```tl
messages.search#a0fda762 flags:# peer:InputPeer q:string from_id:flags.0?InputPeer top_msg_id:flags.1?int filter:MessagesFilter min_date:int max_date:int offset_id:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages;
```

### `messages.readHistory`

```tl
messages.readHistory#e306d3a peer:InputPeer max_id:int = messages.AffectedMessages;
```

### `messages.deleteHistory`

```tl
messages.deleteHistory#b08f922a flags:# just_clear:flags.0?true revoke:flags.1?true peer:InputPeer max_id:int min_date:flags.2?int max_date:flags.3?int = messages.AffectedHistory;
```

### `messages.deleteMessages`

```tl
messages.deleteMessages#e547869b flags:# revoke:flags.0?true id:Vector<int> peer:flags.30?InputPeer = messages.AffectedMessages;
```

### `messages.receivedMessages`

```tl
messages.receivedMessages#5a954c0 max_id:int = Vector<ReceivedNotifyMessage>;
```

### `messages.setTyping`

```tl
messages.setTyping#58943ee2 flags:# peer:InputPeer top_msg_id:flags.0?int action:SendMessageAction = Bool;
```

### `messages.sendMessage`

```tl
messages.sendMessage#280d096f flags:# no_webpage:flags.1?true silent:flags.5?true background:flags.6?true clear_draft:flags.7?true noforwards:flags.14?true update_stickersets_order:flags.15?true invert_media:flags.16?true peer:InputPeer reply_to:flags.0?InputReplyTo message:string random_id:long reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> schedule_date:flags.10?int send_as:flags.13?InputPeer = Updates;
```

### `messages.sendMedia`

```tl
messages.sendMedia#72ccc23d flags:# silent:flags.5?true background:flags.6?true clear_draft:flags.7?true noforwards:flags.14?true update_stickersets_order:flags.15?true invert_media:flags.16?true peer:InputPeer reply_to:flags.0?InputReplyTo media:InputMedia message:string random_id:long reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> schedule_date:flags.10?int send_as:flags.13?InputPeer = Updates;
```

### `messages.forwardMessages`

```tl
messages.forwardMessages#c661bbc4 flags:# silent:flags.5?true background:flags.6?true with_my_score:flags.8?true drop_author:flags.11?true drop_media_captions:flags.12?true noforwards:flags.14?true from_peer:InputPeer id:Vector<int> random_id:Vector<long> to_peer:InputPeer top_msg_id:flags.9?int schedule_date:flags.10?int send_as:flags.13?InputPeer = Updates;
```

### `messages.reportSpam`

```tl
messages.reportSpam#cf1592db peer:InputPeer = Bool;
```

### `messages.getPeerSettings`

```tl
messages.getPeerSettings#efd9a6a2 peer:InputPeer = messages.PeerSettings;
```

### `messages.report`

```tl
messages.report#8953ab4e peer:InputPeer id:Vector<int> reason:ReportReason message:string = Bool;
```

### `messages.getChats`

```tl
messages.getChats#49e9528f id:Vector<long> = messages.Chats;
```

### `messages.getFullChat`

```tl
messages.getFullChat#aeb00b34 chat_id:long = messages.ChatFull;
```

### `messages.editChatTitle`

```tl
messages.editChatTitle#73783ffd chat_id:long title:string = Updates;
```

### `messages.editChatPhoto`

```tl
messages.editChatPhoto#35ddd674 chat_id:long photo:InputChatPhoto = Updates;
```

### `messages.addChatUser`

```tl
messages.addChatUser#f24753e3 chat_id:long user_id:InputUser fwd_limit:int = Updates;
```

### `messages.deleteChatUser`

```tl
messages.deleteChatUser#a2185cab flags:# revoke_history:flags.0?true chat_id:long user_id:InputUser = Updates;
```

### `messages.createChat`

```tl
messages.createChat#34a818 flags:# users:Vector<InputUser> title:string ttl_period:flags.0?int = Updates;
```

### `messages.getDhConfig`

```tl
messages.getDhConfig#26cf8950 version:int random_length:int = messages.DhConfig;
```

### `messages.readMessageContents`

```tl
messages.readMessageContents#36a73f77 id:Vector<int> = messages.AffectedMessages;
```

### `messages.getStickers`

```tl
messages.getStickers#d5a5d3a1 emoticon:string hash:long = messages.Stickers;
```

### `messages.getAllStickers`

```tl
messages.getAllStickers#b8a0a1a8 hash:long = messages.AllStickers;
```

### `messages.getWebPagePreview`

```tl
messages.getWebPagePreview#8b68b0cc flags:# message:string entities:flags.3?Vector<MessageEntity> = MessageMedia;
```

### `messages.exportChatInvite`

```tl
messages.exportChatInvite#a02ce5d5 flags:# legacy_revoke_permanent:flags.2?true request_needed:flags.3?true peer:InputPeer expire_date:flags.0?int usage_limit:flags.1?int title:flags.4?string = ExportedChatInvite;
```

### `messages.checkChatInvite`

```tl
messages.checkChatInvite#3eadb1bb hash:string = ChatInvite;
```

### `messages.importChatInvite`

```tl
messages.importChatInvite#6c50051c hash:string = Updates;
```

### `messages.getStickerSet`

```tl
messages.getStickerSet#c8a0ec74 stickerset:InputStickerSet hash:int = messages.StickerSet;
```

### `messages.installStickerSet`

```tl
messages.installStickerSet#c78fe460 stickerset:InputStickerSet archived:Bool = messages.StickerSetInstallResult;
```

### `messages.uninstallStickerSet`

```tl
messages.uninstallStickerSet#f96e55de stickerset:InputStickerSet = Bool;
```

### `messages.startBot`

```tl
messages.startBot#e6df7378 bot:InputUser peer:InputPeer random_id:long start_param:string = Updates;
```

### `messages.getMessagesViews`

```tl
messages.getMessagesViews#5784d3e1 peer:InputPeer id:Vector<int> increment:Bool = messages.MessageViews;
```

### `messages.migrateChat`

```tl
messages.migrateChat#a2875319 chat_id:long = Updates;
```

### `messages.searchGlobal`

```tl
messages.searchGlobal#4bc6589a flags:# folder_id:flags.0?int q:string filter:MessagesFilter min_date:int max_date:int offset_rate:int offset_peer:InputPeer offset_id:int limit:int = messages.Messages;
```

### `messages.getDocumentByHash`

```tl
messages.getDocumentByHash#b1f2061f sha256:bytes size:long mime_type:string = Document;
```

### `messages.getSavedGifs`

```tl
messages.getSavedGifs#5cf09635 hash:long = messages.SavedGifs;
```

### `messages.saveGif`

```tl
messages.saveGif#327a30cb id:InputDocument unsave:Bool = Bool;
```

### `messages.getInlineBotResults`

```tl
messages.getInlineBotResults#514e999d flags:# bot:InputUser peer:InputPeer geo_point:flags.0?InputGeoPoint query:string offset:string = messages.BotResults;
```

### `messages.sendInlineBotResult`

```tl
messages.sendInlineBotResult#f7bc68ba flags:# silent:flags.5?true background:flags.6?true clear_draft:flags.7?true hide_via:flags.11?true peer:InputPeer reply_to:flags.0?InputReplyTo random_id:long query_id:long id:string schedule_date:flags.10?int send_as:flags.13?InputPeer = Updates;
```

### `messages.editMessage`

```tl
messages.editMessage#48f71778 flags:# no_webpage:flags.1?true invert_media:flags.16?true peer:InputPeer id:int message:flags.11?string media:flags.14?InputMedia reply_markup:flags.2?ReplyMarkup entities:flags.3?Vector<MessageEntity> schedule_date:flags.15?int = Updates;
```

### `messages.getBotCallbackAnswer`

```tl
messages.getBotCallbackAnswer#9342ca07 flags:# game:flags.1?true peer:InputPeer msg_id:int data:flags.0?bytes password:flags.2?InputCheckPasswordSRP = messages.BotCallbackAnswer;
```

### `messages.getPeerDialogs`

```tl
messages.getPeerDialogs#e470bcfd peers:Vector<InputDialogPeer> = messages.PeerDialogs;
```

### `messages.saveDraft`

```tl
messages.saveDraft#7ff3b806 flags:# no_webpage:flags.1?true invert_media:flags.6?true reply_to:flags.4?InputReplyTo peer:InputPeer message:string entities:flags.3?Vector<MessageEntity> media:flags.5?InputMedia = Bool;
```

### `messages.getFeaturedStickers`

```tl
messages.getFeaturedStickers#64780b14 hash:long = messages.FeaturedStickers;
```

### `messages.readFeaturedStickers`

```tl
messages.readFeaturedStickers#5b118126 id:Vector<long> = Bool;
```

### `messages.getRecentStickers`

```tl
messages.getRecentStickers#9da9403b flags:# attached:flags.0?true hash:long = messages.RecentStickers;
```

### `messages.saveRecentSticker`

```tl
messages.saveRecentSticker#392718f8 flags:# attached:flags.0?true id:InputDocument unsave:Bool = Bool;
```

### `messages.clearRecentStickers`

```tl
messages.clearRecentStickers#8999602d flags:# attached:flags.0?true = Bool;
```

### `messages.getArchivedStickers`

```tl
messages.getArchivedStickers#57f17692 flags:# masks:flags.0?true emojis:flags.1?true offset_id:long limit:int = messages.ArchivedStickers;
```

### `messages.getCommonChats`

```tl
messages.getCommonChats#e40ca104 user_id:InputUser max_id:long limit:int = messages.Chats;
```

### `messages.getWebPage`

```tl
messages.getWebPage#8d9692a3 url:string hash:int = messages.WebPage;
```

### `messages.toggleDialogPin`

```tl
messages.toggleDialogPin#a731e257 flags:# pinned:flags.0?true peer:InputDialogPeer = Bool;
```

### `messages.getPinnedDialogs`

```tl
messages.getPinnedDialogs#d6b94df2 folder_id:int = messages.PeerDialogs;
```

### `messages.uploadMedia`

```tl
messages.uploadMedia#519bc2b1 peer:InputPeer media:InputMedia = MessageMedia;
```

### `messages.getFavedStickers`

```tl
messages.getFavedStickers#4f1aaa9 hash:long = messages.FavedStickers;
```

### `messages.faveSticker`

```tl
messages.faveSticker#b9ffc55b id:InputDocument unfave:Bool = Bool;
```

### `messages.getUnreadMentions`

```tl
messages.getUnreadMentions#f107e790 flags:# peer:InputPeer top_msg_id:flags.0?int offset_id:int add_offset:int limit:int max_id:int min_id:int = messages.Messages;
```

### `messages.readMentions`

```tl
messages.readMentions#36e5bf4d flags:# peer:InputPeer top_msg_id:flags.0?int = messages.AffectedHistory;
```

### `messages.sendMultiMedia`

```tl
messages.sendMultiMedia#456e8987 flags:# silent:flags.5?true background:flags.6?true clear_draft:flags.7?true noforwards:flags.14?true update_stickersets_order:flags.15?true invert_media:flags.16?true peer:InputPeer reply_to:flags.0?InputReplyTo multi_media:Vector<InputSingleMedia> schedule_date:flags.10?int send_as:flags.13?InputPeer = Updates;
```

### `messages.searchStickerSets`

```tl
messages.searchStickerSets#35705b8a flags:# exclude_featured:flags.0?true q:string hash:long = messages.FoundStickerSets;
```

### `messages.markDialogUnread`

```tl
messages.markDialogUnread#c286d98f flags:# unread:flags.0?true peer:InputDialogPeer = Bool;
```

### `messages.updatePinnedMessage`

```tl
messages.updatePinnedMessage#d2aaf7ec flags:# silent:flags.0?true unpin:flags.1?true pm_oneside:flags.2?true peer:InputPeer id:int = Updates;
```

### `messages.sendVote`

```tl
messages.sendVote#10ea6184 peer:InputPeer msg_id:int options:Vector<bytes> = Updates;
```

### `messages.getPollResults`

```tl
messages.getPollResults#73bb643b peer:InputPeer msg_id:int = Updates;
```

### `messages.getOnlines`

```tl
messages.getOnlines#6e2be050 peer:InputPeer = ChatOnlines;
```

### `messages.editChatAbout`

```tl
messages.editChatAbout#def60797 peer:InputPeer about:string = Bool;
```

### `messages.editChatDefaultBannedRights`

```tl
messages.editChatDefaultBannedRights#a5866b41 peer:InputPeer banned_rights:ChatBannedRights = Updates;
```

### `messages.getEmojiKeywordsDifference`

```tl
messages.getEmojiKeywordsDifference#1508b6af lang_code:string from_version:int = EmojiKeywordsDifference;
```

### `messages.requestUrlAuth`

```tl
messages.requestUrlAuth#198fb446 flags:# peer:flags.1?InputPeer msg_id:flags.1?int button_id:flags.1?int url:flags.2?string = UrlAuthResult;
```

### `messages.acceptUrlAuth`

```tl
messages.acceptUrlAuth#b12c7125 flags:# write_allowed:flags.0?true peer:flags.1?InputPeer msg_id:flags.1?int button_id:flags.1?int url:flags.2?string = UrlAuthResult;
```

### `messages.hidePeerSettingsBar`

```tl
messages.hidePeerSettingsBar#4facb138 peer:InputPeer = Bool;
```

### `messages.getScheduledHistory`

```tl
messages.getScheduledHistory#f516760b peer:InputPeer hash:long = messages.Messages;
```

### `messages.sendScheduledMessages`

```tl
messages.sendScheduledMessages#bd38850a peer:InputPeer id:Vector<int> = Updates;
```

### `messages.deleteScheduledMessages`

```tl
messages.deleteScheduledMessages#59ae2b16 peer:InputPeer id:Vector<int> = Updates;
```

### `messages.getPollVotes`

```tl
messages.getPollVotes#b86e380e flags:# peer:InputPeer id:int option:flags.0?bytes offset:flags.1?string limit:int = messages.VotesList;
```

### `messages.getDialogFilters`

```tl
messages.getDialogFilters#efd48c89 = messages.DialogFilters;
```

### `messages.getSuggestedDialogFilters`

```tl
messages.getSuggestedDialogFilters#a29cd42c = Vector<DialogFilterSuggested>;
```

### `messages.updateDialogFilter`

```tl
messages.updateDialogFilter#1ad4a04a flags:# id:int filter:flags.0?DialogFilter = Bool;
```

### `messages.updateDialogFiltersOrder`

```tl
messages.updateDialogFiltersOrder#c563c1e4 order:Vector<int> = Bool;
```

### `messages.getReplies`

```tl
messages.getReplies#22ddd30c peer:InputPeer msg_id:int offset_id:int offset_date:int add_offset:int limit:int max_id:int min_id:int hash:long = messages.Messages;
```

### `messages.getDiscussionMessage`

```tl
messages.getDiscussionMessage#446972fd peer:InputPeer msg_id:int = messages.DiscussionMessage;
```

### `messages.readDiscussion`

```tl
messages.readDiscussion#f731a9f4 peer:InputPeer msg_id:int read_max_id:int = Bool;
```

### `messages.unpinAllMessages`

```tl
messages.unpinAllMessages#ee22b9a8 flags:# peer:InputPeer top_msg_id:flags.0?int = messages.AffectedHistory;
```

### `messages.deleteChat`

```tl
messages.deleteChat#5bd0ee50 chat_id:long = Bool;
```

### `messages.getExportedChatInvites`

```tl
messages.getExportedChatInvites#a2b5a3f6 flags:# revoked:flags.3?true peer:InputPeer admin_id:InputUser offset_date:flags.2?int offset_link:flags.2?string limit:int = messages.ExportedChatInvites;
```

### `messages.editExportedChatInvite`

```tl
messages.editExportedChatInvite#bdca2f75 flags:# revoked:flags.2?true peer:InputPeer link:string expire_date:flags.0?int usage_limit:flags.1?int request_needed:flags.3?Bool title:flags.4?string = messages.ExportedChatInvite;
```

### `messages.deleteRevokedExportedChatInvites`

```tl
messages.deleteRevokedExportedChatInvites#56987bd5 peer:InputPeer admin_id:InputUser = Bool;
```

### `messages.deleteExportedChatInvite`

```tl
messages.deleteExportedChatInvite#d464a42b peer:InputPeer link:string = Bool;
```

### `messages.getChatInviteImporters`

```tl
messages.getChatInviteImporters#df04dd4e flags:# requested:flags.0?true peer:InputPeer link:flags.1?string q:flags.2?string offset_date:int offset_user:InputUser limit:int = messages.ChatInviteImporters;
```

### `messages.getMessageReadParticipants`

```tl
messages.getMessageReadParticipants#31c1c44f peer:InputPeer msg_id:int = Vector<ReadParticipantDate>;
```

### `messages.hideChatJoinRequest`

```tl
messages.hideChatJoinRequest#7fe7e815 flags:# approved:flags.0?true peer:InputPeer user_id:InputUser = Updates;
```

### `messages.hideAllChatJoinRequests`

```tl
messages.hideAllChatJoinRequests#e085f4ea flags:# approved:flags.0?true peer:InputPeer link:flags.1?string = Updates;
```

### `messages.toggleNoForwards`

```tl
messages.toggleNoForwards#b11eafa2 peer:InputPeer enabled:Bool = Updates;
```

### `messages.saveDefaultSendAs`

```tl
messages.saveDefaultSendAs#ccfddf96 peer:InputPeer send_as:InputPeer = Bool;
```

### `messages.sendReaction`

```tl
messages.sendReaction#d30d78d4 flags:# big:flags.1?true add_to_recent:flags.2?true peer:InputPeer msg_id:int reaction:flags.0?Vector<Reaction> = Updates;
```

### `messages.getMessagesReactions`

```tl
messages.getMessagesReactions#8bba90e6 peer:InputPeer id:Vector<int> = Updates;
```

### `messages.getMessageReactionsList`

```tl
messages.getMessageReactionsList#461b3f48 flags:# peer:InputPeer id:int reaction:flags.0?Reaction offset:flags.1?string limit:int = messages.MessageReactionsList;
```

### `messages.setChatAvailableReactions`

```tl
messages.setChatAvailableReactions#feb16771 peer:InputPeer available_reactions:ChatReactions = Updates;
```

### `messages.getAvailableReactions`

```tl
messages.getAvailableReactions#18dea0ac hash:int = messages.AvailableReactions;
```

### `messages.setDefaultReaction`

```tl
messages.setDefaultReaction#4f47a016 reaction:Reaction = Bool;
```

### `messages.translateText`

```tl
messages.translateText#63183030 flags:# peer:flags.0?InputPeer id:flags.0?Vector<int> text:flags.1?Vector<TextWithEntities> to_lang:string = messages.TranslatedText;
```

### `messages.getUnreadReactions`

```tl
messages.getUnreadReactions#3223495b flags:# peer:InputPeer top_msg_id:flags.0?int offset_id:int add_offset:int limit:int max_id:int min_id:int = messages.Messages;
```

### `messages.readReactions`

```tl
messages.readReactions#54aa7f8e flags:# peer:InputPeer top_msg_id:flags.0?int = messages.AffectedHistory;
```

### `messages.getAttachMenuBots`

```tl
messages.getAttachMenuBots#16fcc2cb hash:long = AttachMenuBots;
```

### `messages.getAttachMenuBot`

```tl
messages.getAttachMenuBot#77216192 bot:InputUser = AttachMenuBotsBot;
```

### `messages.toggleBotInAttachMenu`

```tl
messages.toggleBotInAttachMenu#69f59d69 flags:# write_allowed:flags.0?true bot:InputUser enabled:Bool = Bool;
```

### `messages.requestWebView`

```tl
messages.requestWebView#269dc2c1 flags:# from_bot_menu:flags.4?true silent:flags.5?true peer:InputPeer bot:InputUser url:flags.1?string start_param:flags.3?string theme_params:flags.2?DataJSON platform:string reply_to:flags.0?InputReplyTo send_as:flags.13?InputPeer = WebViewResult;
```

### `messages.prolongWebView`

```tl
messages.prolongWebView#b0d81a83 flags:# silent:flags.5?true peer:InputPeer bot:InputUser query_id:long reply_to:flags.0?InputReplyTo send_as:flags.13?InputPeer = Bool;
```

### `messages.requestSimpleWebView`

```tl
messages.requestSimpleWebView#1a46500a flags:# from_switch_webview:flags.1?true from_side_menu:flags.2?true bot:InputUser url:flags.3?string start_param:flags.4?string theme_params:flags.0?DataJSON platform:string = SimpleWebViewResult;
```

### `messages.sendWebViewResultMessage`

```tl
messages.sendWebViewResultMessage#a4314f5 bot_query_id:string result:InputBotInlineResult = WebViewMessageSent;
```

### `messages.sendWebViewData`

```tl
messages.sendWebViewData#dc0242c8 bot:InputUser random_id:long button_text:string data:string = Updates;
```

### `messages.transcribeAudio`

```tl
messages.transcribeAudio#269e9a49 peer:InputPeer msg_id:int = messages.TranscribedAudio;
```

### `messages.getCustomEmojiDocuments`

```tl
messages.getCustomEmojiDocuments#d9ab0f54 document_id:Vector<long> = Vector<Document>;
```

### `messages.getEmojiStickers`

```tl
messages.getEmojiStickers#fbfca18f hash:long = messages.AllStickers;
```

### `messages.getFeaturedEmojiStickers`

```tl
messages.getFeaturedEmojiStickers#ecf6736 hash:long = messages.FeaturedStickers;
```

### `messages.getTopReactions`

```tl
messages.getTopReactions#bb8125ba limit:int hash:long = messages.Reactions;
```

### `messages.getRecentReactions`

```tl
messages.getRecentReactions#39461db2 limit:int hash:long = messages.Reactions;
```

### `messages.clearRecentReactions`

```tl
messages.clearRecentReactions#9dfeefb4 = Bool;
```

### `messages.getExtendedMedia`

```tl
messages.getExtendedMedia#84f80814 peer:InputPeer id:Vector<int> = Updates;
```

### `messages.togglePeerTranslations`

```tl
messages.togglePeerTranslations#e47cb579 flags:# disabled:flags.0?true peer:InputPeer = Bool;
```

### `messages.getBotApp`

```tl
messages.getBotApp#34fdc5c3 app:InputBotApp hash:long = messages.BotApp;
```

### `messages.requestAppWebView`

```tl
messages.requestAppWebView#8c5a3b3c flags:# write_allowed:flags.0?true peer:InputPeer app:InputBotApp start_param:flags.1?string theme_params:flags.2?DataJSON platform:string = AppWebViewResult;
```

### `updates.getState`

```tl
updates.getState#edd4882a = updates.State;
```

### `updates.getDifference`

```tl
updates.getDifference#19c2f763 flags:# pts:int pts_limit:flags.1?int pts_total_limit:flags.0?int date:int qts:int qts_limit:flags.2?int = updates.Difference;
```

### `updates.getChannelDifference`

```tl
updates.getChannelDifference#3173d78 flags:# force:flags.0?true channel:InputChannel filter:ChannelMessagesFilter pts:int limit:int = updates.ChannelDifference;
```

### `photos.updateProfilePhoto`

```tl
photos.updateProfilePhoto#9e82039 flags:# fallback:flags.0?true bot:flags.1?InputUser id:InputPhoto = photos.Photo;
```

### `photos.uploadProfilePhoto`

```tl
photos.uploadProfilePhoto#388a3b5 flags:# fallback:flags.3?true bot:flags.5?InputUser file:flags.0?InputFile video:flags.1?InputFile video_start_ts:flags.2?double video_emoji_markup:flags.4?VideoSize = photos.Photo;
```

### `photos.deletePhotos`

```tl
photos.deletePhotos#87cf7f2f id:Vector<InputPhoto> = Vector<long>;
```

### `photos.getUserPhotos`

```tl
photos.getUserPhotos#91cd32a8 user_id:InputUser offset:int max_id:long limit:int = photos.Photos;
```

### `photos.uploadContactProfilePhoto`

```tl
photos.uploadContactProfilePhoto#e14c4a71 flags:# suggest:flags.3?true save:flags.4?true user_id:InputUser file:flags.0?InputFile video:flags.1?InputFile video_start_ts:flags.2?double video_emoji_markup:flags.5?VideoSize = photos.Photo;
```

### `upload.saveFilePart`

```tl
upload.saveFilePart#b304a621 file_id:long file_part:int bytes:bytes = Bool;
```

### `upload.getFile`

```tl
upload.getFile#be5335be flags:# precise:flags.0?true cdn_supported:flags.1?true location:InputFileLocation offset:long limit:int = upload.File;
```

### `upload.saveBigFilePart`

```tl
upload.saveBigFilePart#de7b673d file_id:long file_part:int file_total_parts:int bytes:bytes = Bool;
```

### `upload.getWebFile`

```tl
upload.getWebFile#24e6818d location:InputWebFileLocation offset:int limit:int = upload.WebFile;
```

### `help.getConfig`

```tl
help.getConfig#c4f9186b = Config;
```

### `help.getNearestDc`

```tl
help.getNearestDc#1fb33026 = NearestDc;
```

### `help.getSupport`

```tl
help.getSupport#9cdf08cd = help.Support;
```

### `help.acceptTermsOfService`

```tl
help.acceptTermsOfService#ee72f79a id:DataJSON = Bool;
```

### `help.getAppConfig`

```tl
help.getAppConfig#61e3f854 hash:int = help.AppConfig;
```

### `help.getCountriesList`

```tl
help.getCountriesList#735787a8 lang_code:string hash:int = help.CountriesList;
```

### `help.getPremiumPromo`

```tl
help.getPremiumPromo#b81b93d4 = help.PremiumPromo;
```

### `help.getPeerColors`

```tl
help.getPeerColors#da80f42f hash:int = help.PeerColors;
```

### `help.getPeerProfileColors`

```tl
help.getPeerProfileColors#abcfa9fd hash:int = help.PeerColors;
```

### `channels.readHistory`

```tl
channels.readHistory#cc104937 channel:InputChannel max_id:int = Bool;
```

### `channels.deleteMessages`

```tl
channels.deleteMessages#84c1fd4e channel:InputChannel id:Vector<int> = messages.AffectedMessages;
```

### `channels.getMessages`

```tl
channels.getMessages#ad8c9a23 channel:InputChannel id:Vector<InputMessage> = messages.Messages;
```

### `channels.getParticipants`

```tl
channels.getParticipants#77ced9d0 channel:InputChannel filter:ChannelParticipantsFilter offset:int limit:int hash:long = channels.ChannelParticipants;
```

### `channels.getParticipant`

```tl
channels.getParticipant#a0ab6cc6 channel:InputChannel participant:InputPeer = channels.ChannelParticipant;
```

### `channels.getChannels`

```tl
channels.getChannels#a7f6bbb id:Vector<InputChannel> = messages.Chats;
```

### `channels.getFullChannel`

```tl
channels.getFullChannel#8736a09 channel:InputChannel = messages.ChatFull;
```

### `channels.createChannel`

```tl
channels.createChannel#91006707 flags:# broadcast:flags.0?true megagroup:flags.1?true for_import:flags.3?true forum:flags.5?true title:string about:string geo_point:flags.2?InputGeoPoint address:flags.2?string ttl_period:flags.4?int = Updates;
```

### `channels.editAdmin`

```tl
channels.editAdmin#d33c8902 channel:InputChannel user_id:InputUser admin_rights:ChatAdminRights rank:string = Updates;
```

### `channels.editTitle`

```tl
channels.editTitle#566decd0 channel:InputChannel title:string = Updates;
```

### `channels.editPhoto`

```tl
channels.editPhoto#f12e57c9 channel:InputChannel photo:InputChatPhoto = Updates;
```

### `channels.checkUsername`

```tl
channels.checkUsername#10e6bd2c channel:InputChannel username:string = Bool;
```

### `channels.updateUsername`

```tl
channels.updateUsername#3514b3de channel:InputChannel username:string = Bool;
```

### `channels.joinChannel`

```tl
channels.joinChannel#24b524c5 channel:InputChannel = Updates;
```

### `channels.leaveChannel`

```tl
channels.leaveChannel#f836aa95 channel:InputChannel = Updates;
```

### `channels.inviteToChannel`

```tl
channels.inviteToChannel#199f3a6c channel:InputChannel users:Vector<InputUser> = Updates;
```

### `channels.deleteChannel`

```tl
channels.deleteChannel#c0111fe3 channel:InputChannel = Updates;
```

### `channels.toggleSignatures`

```tl
channels.toggleSignatures#1f69b606 channel:InputChannel enabled:Bool = Updates;
```

### `channels.getAdminedPublicChannels`

```tl
channels.getAdminedPublicChannels#f8b036af flags:# by_location:flags.0?true check_limit:flags.1?true for_personal:flags.2?true = messages.Chats;
```

### `channels.editBanned`

```tl
channels.editBanned#96e6cd81 channel:InputChannel participant:InputPeer banned_rights:ChatBannedRights = Updates;
```

### `channels.readMessageContents`

```tl
channels.readMessageContents#eab5dc38 channel:InputChannel id:Vector<int> = Bool;
```

### `channels.togglePreHistoryHidden`

```tl
channels.togglePreHistoryHidden#eabbb94c channel:InputChannel enabled:Bool = Updates;
```

### `channels.getGroupsForDiscussion`

```tl
channels.getGroupsForDiscussion#f5dad378 = messages.Chats;
```

### `channels.setDiscussionGroup`

```tl
channels.setDiscussionGroup#40582bb2 broadcast:InputChannel group:InputChannel = Bool;
```

### `channels.viewSponsoredMessage`

```tl
channels.viewSponsoredMessage#beaedb94 channel:InputChannel random_id:bytes = Bool;
```

### `channels.getSponsoredMessages`

```tl
channels.getSponsoredMessages#ec210fbf channel:InputChannel = messages.SponsoredMessages;
```

### `channels.getSendAs`

```tl
channels.getSendAs#dc770ee peer:InputPeer = channels.SendAsPeers;
```

### `channels.toggleJoinToSend`

```tl
channels.toggleJoinToSend#e4cb9580 channel:InputChannel enabled:Bool = Updates;
```

### `channels.toggleJoinRequest`

```tl
channels.toggleJoinRequest#4c2985b6 channel:InputChannel enabled:Bool = Updates;
```

### `channels.reorderUsernames`

```tl
channels.reorderUsernames#b45ced1d channel:InputChannel order:Vector<string> = Bool;
```

### `channels.toggleUsername`

```tl
channels.toggleUsername#50f24105 channel:InputChannel username:string active:Bool = Bool;
```

### `channels.deactivateAllUsernames`

```tl
channels.deactivateAllUsernames#a245dd3 channel:InputChannel = Bool;
```

### `channels.toggleForum`

```tl
channels.toggleForum#a4298b29 channel:InputChannel enabled:Bool = Updates;
```

### `channels.createForumTopic`

```tl
channels.createForumTopic#f40c0224 flags:# channel:InputChannel title:string icon_color:flags.0?int icon_emoji_id:flags.3?long random_id:long send_as:flags.2?InputPeer = Updates;
```

### `channels.getForumTopics`

```tl
channels.getForumTopics#de560d1 flags:# channel:InputChannel q:flags.0?string offset_date:int offset_id:int offset_topic:int limit:int = messages.ForumTopics;
```

### `channels.getForumTopicsByID`

```tl
channels.getForumTopicsByID#b0831eb9 channel:InputChannel topics:Vector<int> = messages.ForumTopics;
```

### `channels.editForumTopic`

```tl
channels.editForumTopic#f4dfa185 flags:# channel:InputChannel topic_id:int title:flags.0?string icon_emoji_id:flags.1?long closed:flags.2?Bool hidden:flags.3?Bool = Updates;
```

### `channels.updatePinnedForumTopic`

```tl
channels.updatePinnedForumTopic#6c2d9026 channel:InputChannel topic_id:int pinned:Bool = Updates;
```

### `channels.deleteTopicHistory`

```tl
channels.deleteTopicHistory#34435f2d channel:InputChannel top_msg_id:int = messages.AffectedHistory;
```

### `channels.toggleParticipantsHidden`

```tl
channels.toggleParticipantsHidden#6a6e7854 channel:InputChannel enabled:Bool = Updates;
```

### `channels.clickSponsoredMessage`

```tl
channels.clickSponsoredMessage#18afbc93 channel:InputChannel random_id:bytes = Bool;
```

### `channels.toggleViewForumAsMessages`

```tl
channels.toggleViewForumAsMessages#9738bb15 channel:InputChannel enabled:Bool = Updates;
```

### `channels.toggleMembershipMessageVisibility`

```tl
channels.toggleMembershipMessageVisibility#75646c0 channel:InputChannel enabled:Bool = Updates;
```

### `bots.canSendMessage`

```tl
bots.canSendMessage#1359f4e6 bot:InputUser = Bool;
```

### `bots.allowSendMessage`

```tl
bots.allowSendMessage#f132e3ef bot:InputUser = Updates;
```

### `bots.invokeWebViewCustomMethod`

```tl
bots.invokeWebViewCustomMethod#87fc5e7 bot:InputUser custom_method:string params:DataJSON = DataJSON;
```

### `payments.getPaymentForm`

```tl
payments.getPaymentForm#37148dbb flags:# invoice:InputInvoice theme_params:flags.0?DataJSON = payments.PaymentForm;
```

### `payments.getPaymentReceipt`

```tl
payments.getPaymentReceipt#2478d1cc peer:InputPeer msg_id:int = payments.PaymentReceipt;
```

### `payments.validateRequestedInfo`

```tl
payments.validateRequestedInfo#b6c8f12b flags:# save:flags.0?true invoice:InputInvoice info:PaymentRequestedInfo = payments.ValidatedRequestedInfo;
```

### `payments.sendPaymentForm`

```tl
payments.sendPaymentForm#2d03522f flags:# form_id:long invoice:InputInvoice requested_info_id:flags.0?string shipping_option_id:flags.1?string credentials:InputPaymentCredentials tip_amount:flags.2?long = payments.PaymentResult;
```

### `payments.getSavedInfo`

```tl
payments.getSavedInfo#227d824b = payments.SavedInfo;
```

### `payments.checkGiftCode`

```tl
payments.checkGiftCode#8e51b4c1 slug:string = payments.CheckedGiftCode;
```

### `payments.applyGiftCode`

```tl
payments.applyGiftCode#f6e26854 slug:string = Updates;
```

### `payments.getGiveawayInfo`

```tl
payments.getGiveawayInfo#f4239425 peer:InputPeer msg_id:int = payments.GiveawayInfo;
```

### `phone.requestCall`

```tl
phone.requestCall#42ff96ed flags:# video:flags.0?true user_id:InputUser random_id:int g_a_hash:bytes protocol:PhoneCallProtocol = phone.PhoneCall;
```

### `phone.acceptCall`

```tl
phone.acceptCall#3bd2b4a0 peer:InputPhoneCall g_b:bytes protocol:PhoneCallProtocol = phone.PhoneCall;
```

### `phone.confirmCall`

```tl
phone.confirmCall#2efe1722 peer:InputPhoneCall g_a:bytes key_fingerprint:long protocol:PhoneCallProtocol = phone.PhoneCall;
```

### `phone.receivedCall`

```tl
phone.receivedCall#17d54f61 peer:InputPhoneCall = Bool;
```

### `phone.discardCall`

```tl
phone.discardCall#b2cbc1c0 flags:# video:flags.0?true peer:InputPhoneCall duration:int reason:PhoneCallDiscardReason connection_id:long = Updates;
```

### `phone.setCallRating`

```tl
phone.setCallRating#59ead627 flags:# user_initiative:flags.0?true peer:InputPhoneCall rating:int comment:string = Updates;
```

### `phone.saveCallDebug`

```tl
phone.saveCallDebug#277add7e peer:InputPhoneCall debug:DataJSON = Bool;
```

### `phone.sendSignalingData`

```tl
phone.sendSignalingData#ff7a9383 peer:InputPhoneCall data:bytes = Bool;
```

### `phone.createGroupCall`

```tl
phone.createGroupCall#48cdc6d8 flags:# rtmp_stream:flags.2?true peer:InputPeer random_id:int title:flags.0?string schedule_date:flags.1?int = Updates;
```

### `phone.joinGroupCall`

```tl
phone.joinGroupCall#b132ff7b flags:# muted:flags.0?true video_stopped:flags.2?true call:InputGroupCall join_as:InputPeer invite_hash:flags.1?string params:DataJSON = Updates;
```

### `phone.leaveGroupCall`

```tl
phone.leaveGroupCall#500377f9 call:InputGroupCall source:int = Updates;
```

### `phone.discardGroupCall`

```tl
phone.discardGroupCall#7a777135 call:InputGroupCall = Updates;
```

### `phone.getGroupCall`

```tl
phone.getGroupCall#41845db call:InputGroupCall limit:int = phone.GroupCall;
```

### `phone.getGroupParticipants`

```tl
phone.getGroupParticipants#c558d8ab call:InputGroupCall ids:Vector<InputPeer> sources:Vector<int> offset:string limit:int = phone.GroupParticipants;
```

### `phone.editGroupCallParticipant`

```tl
phone.editGroupCallParticipant#a5273abf flags:# call:InputGroupCall participant:InputPeer muted:flags.0?Bool volume:flags.1?int raise_hand:flags.2?Bool video_stopped:flags.3?Bool video_paused:flags.4?Bool presentation_paused:flags.5?Bool = Updates;
```

### `phone.exportGroupCallInvite`

```tl
phone.exportGroupCallInvite#e6aa647f flags:# can_self_unmute:flags.0?true call:InputGroupCall = phone.ExportedGroupCallInvite;
```

### `phone.toggleGroupCallStartSubscription`

```tl
phone.toggleGroupCallStartSubscription#219c34e6 call:InputGroupCall subscribed:Bool = Updates;
```

### `phone.joinGroupCallPresentation`

```tl
phone.joinGroupCallPresentation#cbea6bc4 call:InputGroupCall params:DataJSON = Updates;
```

### `phone.leaveGroupCallPresentation`

```tl
phone.leaveGroupCallPresentation#1c50d144 call:InputGroupCall = Updates;
```

### `langpack.getLangPack`

```tl
langpack.getLangPack#f2f2330a lang_pack:string lang_code:string = LangPackDifference;
```

### `langpack.getStrings`

```tl
langpack.getStrings#efea3803 lang_pack:string lang_code:string keys:Vector<string> = Vector<LangPackString>;
```

### `langpack.getDifference`

```tl
langpack.getDifference#cd984aa5 lang_pack:string lang_code:string from_version:int = LangPackDifference;
```

### `langpack.getLanguages`

```tl
langpack.getLanguages#42c6978f lang_pack:string = Vector<LangPackLanguage>;
```

### `folders.editPeerFolders`

```tl
folders.editPeerFolders#6847d0ab folder_peers:Vector<InputFolderPeer> = Updates;
```

### `stats.getBroadcastStats`

```tl
stats.getBroadcastStats#ab42441a flags:# dark:flags.0?true channel:InputChannel = stats.BroadcastStats;
```

### `stats.loadAsyncGraph`

```tl
stats.loadAsyncGraph#621d5fa0 flags:# token:string x:flags.0?long = StatsGraph;
```

### `stats.getMegagroupStats`

```tl
stats.getMegagroupStats#dcdf8607 flags:# dark:flags.0?true channel:InputChannel = stats.MegagroupStats;
```

### `stats.getMessagePublicForwards`

```tl
stats.getMessagePublicForwards#5630281b channel:InputChannel msg_id:int offset_rate:int offset_peer:InputPeer offset_id:int limit:int = messages.Messages;
```

### `stats.getMessageStats`

```tl
stats.getMessageStats#b6e0a3f5 flags:# dark:flags.0?true channel:InputChannel msg_id:int = stats.MessageStats;
```

### `stats.getStoryStats`

```tl
stats.getStoryStats#374fef40 flags:# dark:flags.0?true peer:InputPeer id:int = stats.StoryStats;
```

### `stats.getStoryPublicForwards`

```tl
stats.getStoryPublicForwards#a6437ef6 peer:InputPeer id:int offset:string limit:int = stats.PublicForwards;
```

### `chatlists.exportChatlistInvite`

```tl
chatlists.exportChatlistInvite#8472478e chatlist:InputChatlist title:string peers:Vector<InputPeer> = chatlists.ExportedChatlistInvite;
```

### `chatlists.deleteExportedInvite`

```tl
chatlists.deleteExportedInvite#719c5c5e chatlist:InputChatlist slug:string = Bool;
```

### `chatlists.editExportedInvite`

```tl
chatlists.editExportedInvite#653db63d flags:# chatlist:InputChatlist slug:string title:flags.1?string peers:flags.2?Vector<InputPeer> = ExportedChatlistInvite;
```

### `chatlists.getExportedInvites`

```tl
chatlists.getExportedInvites#ce03da83 chatlist:InputChatlist = chatlists.ExportedInvites;
```

### `chatlists.checkChatlistInvite`

```tl
chatlists.checkChatlistInvite#41c10fff slug:string = chatlists.ChatlistInvite;
```

### `chatlists.joinChatlistInvite`

```tl
chatlists.joinChatlistInvite#a6b1e39a slug:string peers:Vector<InputPeer> = Updates;
```

### `chatlists.getLeaveChatlistSuggestions`

```tl
chatlists.getLeaveChatlistSuggestions#fdbcd714 chatlist:InputChatlist = Vector<Peer>;
```

### `chatlists.leaveChatlist`

```tl
chatlists.leaveChatlist#74fae13a chatlist:InputChatlist peers:Vector<InputPeer> = Updates;
```

### `stories.editStory`

```tl
stories.editStory#b583ba46 flags:# peer:InputPeer id:int media:flags.0?InputMedia media_areas:flags.3?Vector<MediaArea> caption:flags.1?string entities:flags.1?Vector<MessageEntity> privacy_rules:flags.2?Vector<InputPrivacyRule> = Updates;
```

### `stories.deleteStories`

```tl
stories.deleteStories#ae59db5f peer:InputPeer id:Vector<int> = Vector<int>;
```

### `stories.togglePinned`

```tl
stories.togglePinned#9a75a1ef peer:InputPeer id:Vector<int> pinned:Bool = Vector<int>;
```

### `stories.getAllStories`

```tl
stories.getAllStories#eeb0d625 flags:# next:flags.1?true hidden:flags.2?true state:flags.0?string = stories.AllStories;
```

### `stories.getPinnedStories`

```tl
stories.getPinnedStories#5821a5dc peer:InputPeer offset_id:int limit:int = stories.Stories;
```

### `stories.getStoriesArchive`

```tl
stories.getStoriesArchive#b4352016 peer:InputPeer offset_id:int limit:int = stories.Stories;
```

### `stories.getStoriesByID`

```tl
stories.getStoriesByID#5774ca74 peer:InputPeer id:Vector<int> = stories.Stories;
```

### `stories.readStories`

```tl
stories.readStories#a556dac8 peer:InputPeer max_id:int = Vector<int>;
```

### `stories.incrementStoryViews`

```tl
stories.incrementStoryViews#b2028afb peer:InputPeer id:Vector<int> = Bool;
```

### `stories.getStoryViewsList`

```tl
stories.getStoryViewsList#7ed23c57 flags:# just_contacts:flags.0?true reactions_first:flags.2?true peer:InputPeer q:flags.1?string id:int offset:string limit:int = stories.StoryViewsList;
```

### `stories.exportStoryLink`

```tl
stories.exportStoryLink#7b8def20 peer:InputPeer id:int = ExportedStoryLink;
```

### `stories.report`

```tl
stories.report#1923fa8c peer:InputPeer id:Vector<int> reason:ReportReason message:string = Bool;
```

### `stories.activateStealthMode`

```tl
stories.activateStealthMode#57bbd166 flags:# past:flags.0?true future:flags.1?true = Updates;
```

### `stories.sendReaction`

```tl
stories.sendReaction#7fd736b2 flags:# add_to_recent:flags.0?true peer:InputPeer story_id:int reaction:Reaction = Updates;
```

### `stories.getPeerStories`

```tl
stories.getPeerStories#2c4ada50 peer:InputPeer = stories.PeerStories;
```

### `stories.getPeerMaxIDs`

```tl
stories.getPeerMaxIDs#535983c3 id:Vector<InputPeer> = Vector<int>;
```

### `stories.togglePeerStoriesHidden`

```tl
stories.togglePeerStoriesHidden#bd0415c4 peer:InputPeer hidden:Bool = Bool;
```

### `premium.getBoostsList`

```tl
premium.getBoostsList#60f67660 flags:# gifts:flags.0?true peer:InputPeer offset:string limit:int = premium.BoostsList;
```

### `premium.getMyBoosts`

```tl
premium.getMyBoosts#be77b4a = premium.MyBoosts;
```

### `premium.applyBoost`

```tl
premium.applyBoost#6b7da746 flags:# slots:flags.0?Vector<int> peer:InputPeer = premium.MyBoosts;
```

### `premium.getBoostsStatus`

```tl
premium.getBoostsStatus#42f1f61 peer:InputPeer = premium.BoostsStatus;
```

### `thirdParty.request`

```tl
thirdParty.request#c8520739 message:ThirdPartyMessage = ThirdPartyReply;
```

### `thirdParty.tell`

```tl
thirdParty.tell#a7ebdf75 message:ThirdPartyMessage = Bool;
```

### `help.getTimezonesList`

```tl
help.getTimezonesList#49b30240 hash:int = help.TimezonesList;
```

### `account.updateBusinessWorkHours`

```tl
account.updateBusinessWorkHours#4b00e066 flags:# business_work_hours:flags.0?BusinessWorkHours = Bool;
```

### `account.updateBirthday`

```tl
account.updateBirthday#cc6e0c11 flags:# birthday:flags.0?Birthday = Bool;
```

### `contacts.getBirthdays`

```tl
contacts.getBirthdays#daeda864 = contacts.ContactBirthdays;
```

### `account.saveMusic`

```tl
account.saveMusic#b26732a9 flags:# unsave:flags.0?true id:InputDocument after_id:flags.1?InputDocument = Bool;
```

### `account.setMainProfileTab`

```tl
account.setMainProfileTab#5dee78b0 tab:ProfileTab = Bool;
```

### `account.getSavedMusicIds`

```tl
account.getSavedMusicIds#e09d5faf hash:long = account.SavedMusicIds;
```

### `account.updatePersonalChannel`

```tl
account.updatePersonalChannel#d94305e0 channel:InputChannel = Bool;
```

### `users.getSavedMusic`

```tl
users.getSavedMusic#788d7fe3 id:InputUser offset:int limit:int hash:long = users.SavedMusic;
```

### `users.getSavedMusicByID`

```tl
users.getSavedMusicByID#7573a4e9 id:InputUser documents:Vector<InputDocument> = users.SavedMusic;
```

### `messages.toggleDialogFilterTags`

```tl
messages.toggleDialogFilterTags#fd2dda49 enabled:Bool = Bool;
```

### `req_pq`

```tl
req_pq#60469778 nonce:int128 = ResPQ;
```

### `req_pq_multi`

```tl
req_pq_multi#be7e8ef1 nonce:int128 = ResPQ;
```

### `req_pq_multi_new`

```tl
req_pq_multi_new#51b410fd nonce:int128 = ResPQ;
```

### `req_DH_params`

```tl
req_DH_params#d712e4be nonce:int128 server_nonce:int128 p:string q:string public_key_fingerprint:long encrypted_data:string = Server_DH_Params;
```

### `set_client_DH_params`

```tl
set_client_DH_params#f5045f1f nonce:int128 server_nonce:int128 encrypted_data:string = Set_client_DH_params_answer;
```

### `destroy_auth_key`

```tl
destroy_auth_key#d1435160 = DestroyAuthKeyRes;
```

### `ping`

```tl
ping#7abe77ec ping_id:long = Pong;
```

### `ping_delay_disconnect`

```tl
ping_delay_disconnect#f3427b8c ping_id:long disconnect_delay:int = Pong;
```
