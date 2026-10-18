"""Generated synchronous API signatures."""
from typing import Any


class SyncMethods:
    def invoke_after_msg(self, *, msg_id: Any, query: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.invoke_after_msg(msg_id=msg_id, query=query, wait=wait, timeout=timeout))

    def init_connection(self, *, api_id: Any, device_model: Any, system_version: Any, app_version: Any, system_lang_code: Any, lang_pack: Any, lang_code: Any, query: Any, proxy: Any=None, params: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.init_connection(api_id=api_id, device_model=device_model, system_version=system_version, app_version=app_version, system_lang_code=system_lang_code, lang_pack=lang_pack, lang_code=lang_code, query=query, proxy=proxy, params=params, wait=wait, timeout=timeout))

    def invoke_with_layer(self, *, layer: Any, query: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.invoke_with_layer(layer=layer, query=query, wait=wait, timeout=timeout))

    def auth_send_code(self, *, phone_number: Any, api_id: Any, api_hash: Any, settings: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_send_code(phone_number=phone_number, api_id=api_id, api_hash=api_hash, settings=settings, wait=wait, timeout=timeout))

    def auth_sign_up(self, *, phone_number: Any, phone_code_hash: Any, first_name: Any, last_name: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_sign_up(phone_number=phone_number, phone_code_hash=phone_code_hash, first_name=first_name, last_name=last_name, wait=wait, timeout=timeout))

    def auth_sign_in(self, *, phone_number: Any, phone_code_hash: Any, phone_code: Any=None, email_verification: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_sign_in(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code, email_verification=email_verification, wait=wait, timeout=timeout))

    def auth_log_out(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_log_out(wait=wait, timeout=timeout))

    def auth_reset_authorizations(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_reset_authorizations(wait=wait, timeout=timeout))

    def auth_export_authorization(self, *, dc_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_export_authorization(dc_id=dc_id, wait=wait, timeout=timeout))

    def auth_import_authorization(self, *, id: Any, bytes: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_import_authorization(id=id, bytes=bytes, wait=wait, timeout=timeout))

    def auth_bind_temp_auth_key(self, *, perm_auth_key_id: Any, nonce: Any, expires_at: Any, encrypted_message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_bind_temp_auth_key(perm_auth_key_id=perm_auth_key_id, nonce=nonce, expires_at=expires_at, encrypted_message=encrypted_message, wait=wait, timeout=timeout))

    def auth_check_password(self, *, password: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_check_password(password=password, wait=wait, timeout=timeout))

    def auth_request_password_recovery(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_request_password_recovery(wait=wait, timeout=timeout))

    def auth_resend_code(self, *, phone_number: Any, phone_code_hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_resend_code(phone_number=phone_number, phone_code_hash=phone_code_hash, wait=wait, timeout=timeout))

    def auth_cancel_code(self, *, phone_number: Any, phone_code_hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_cancel_code(phone_number=phone_number, phone_code_hash=phone_code_hash, wait=wait, timeout=timeout))

    def auth_drop_temp_auth_keys(self, *, except_auth_keys: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_drop_temp_auth_keys(except_auth_keys=except_auth_keys, wait=wait, timeout=timeout))

    def auth_export_login_token(self, *, api_id: Any, api_hash: Any, except_ids: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_export_login_token(api_id=api_id, api_hash=api_hash, except_ids=except_ids, wait=wait, timeout=timeout))

    def auth_import_login_token(self, *, token: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_import_login_token(token=token, wait=wait, timeout=timeout))

    def auth_import_web_token_authorization(self, *, api_id: Any, api_hash: Any, web_auth_token: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_import_web_token_authorization(api_id=api_id, api_hash=api_hash, web_auth_token=web_auth_token, wait=wait, timeout=timeout))

    def auth_send_delete_account_code(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_send_delete_account_code(wait=wait, timeout=timeout))

    def auth_resend_delete_account_code(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_resend_delete_account_code(wait=wait, timeout=timeout))

    def auth_delete_account(self, *, delete_account_code: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.auth_delete_account(delete_account_code=delete_account_code, wait=wait, timeout=timeout))

    def account_register_device(self, *, token_type: Any, token: Any, app_sandbox: Any, secret: Any, other_uids: Any, no_muted: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_register_device(token_type=token_type, token=token, app_sandbox=app_sandbox, secret=secret, other_uids=other_uids, no_muted=no_muted, wait=wait, timeout=timeout))

    def account_unregister_device(self, *, token_type: Any, token: Any, other_uids: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_unregister_device(token_type=token_type, token=token, other_uids=other_uids, wait=wait, timeout=timeout))

    def account_update_notify_settings(self, *, peer: Any, settings: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_notify_settings(peer=peer, settings=settings, wait=wait, timeout=timeout))

    def account_get_notify_settings(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_notify_settings(peer=peer, wait=wait, timeout=timeout))

    def account_update_profile(self, *, first_name: Any=None, last_name: Any=None, about: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_profile(first_name=first_name, last_name=last_name, about=about, wait=wait, timeout=timeout))

    def account_update_status(self, *, offline: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_status(offline=offline, wait=wait, timeout=timeout))

    def account_get_wall_papers(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_wall_papers(hash=hash, wait=wait, timeout=timeout))

    def account_report_peer(self, *, peer: Any, reason: Any, message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_report_peer(peer=peer, reason=reason, message=message, wait=wait, timeout=timeout))

    def account_check_username(self, *, username: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_check_username(username=username, wait=wait, timeout=timeout))

    def account_update_username(self, *, username: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_username(username=username, wait=wait, timeout=timeout))

    def account_get_privacy(self, *, key: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_privacy(key=key, wait=wait, timeout=timeout))

    def account_set_privacy(self, *, key: Any, rules: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_set_privacy(key=key, rules=rules, wait=wait, timeout=timeout))

    def account_get_authorizations(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_authorizations(wait=wait, timeout=timeout))

    def account_reset_authorization(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_reset_authorization(hash=hash, wait=wait, timeout=timeout))

    def account_get_password(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_password(wait=wait, timeout=timeout))

    def account_get_password_settings(self, *, password: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_password_settings(password=password, wait=wait, timeout=timeout))

    def account_update_password_settings(self, *, password: Any, new_settings: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_password_settings(password=password, new_settings=new_settings, wait=wait, timeout=timeout))

    def account_send_confirm_phone_code(self, *, hash: Any, settings: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_send_confirm_phone_code(hash=hash, settings=settings, wait=wait, timeout=timeout))

    def account_confirm_phone(self, *, phone_code_hash: Any, phone_code: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_confirm_phone(phone_code_hash=phone_code_hash, phone_code=phone_code, wait=wait, timeout=timeout))

    def account_get_tmp_password(self, *, password: Any, period: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_tmp_password(password=password, period=period, wait=wait, timeout=timeout))

    def account_get_web_authorizations(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_web_authorizations(wait=wait, timeout=timeout))

    def account_reset_web_authorization(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_reset_web_authorization(hash=hash, wait=wait, timeout=timeout))

    def account_reset_web_authorizations(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_reset_web_authorizations(wait=wait, timeout=timeout))

    def account_send_verify_phone_code(self, *, phone_number: Any, settings: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_send_verify_phone_code(phone_number=phone_number, settings=settings, wait=wait, timeout=timeout))

    def account_confirm_password_email(self, *, code: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_confirm_password_email(code=code, wait=wait, timeout=timeout))

    def account_get_contact_sign_up_notification(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_contact_sign_up_notification(wait=wait, timeout=timeout))

    def account_set_contact_sign_up_notification(self, *, silent: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_set_contact_sign_up_notification(silent=silent, wait=wait, timeout=timeout))

    def account_get_notify_exceptions(self, *, compare_sound: Any=None, compare_stories: Any=None, peer: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_notify_exceptions(compare_sound=compare_sound, compare_stories=compare_stories, peer=peer, wait=wait, timeout=timeout))

    def account_upload_wall_paper(self, *, file: Any, mime_type: Any, settings: Any, for_chat: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_upload_wall_paper(file=file, mime_type=mime_type, settings=settings, for_chat=for_chat, wait=wait, timeout=timeout))

    def account_get_auto_download_settings(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_auto_download_settings(wait=wait, timeout=timeout))

    def account_save_auto_download_settings(self, *, settings: Any, low: Any=None, high: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_save_auto_download_settings(settings=settings, low=low, high=high, wait=wait, timeout=timeout))

    def account_set_content_settings(self, *, sensitive_enabled: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_set_content_settings(sensitive_enabled=sensitive_enabled, wait=wait, timeout=timeout))

    def account_get_content_settings(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_content_settings(wait=wait, timeout=timeout))

    def account_get_global_privacy_settings(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_global_privacy_settings(wait=wait, timeout=timeout))

    def account_set_global_privacy_settings(self, *, settings: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_set_global_privacy_settings(settings=settings, wait=wait, timeout=timeout))

    def account_report_profile_photo(self, *, peer: Any, photo_id: Any, reason: Any, message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_report_profile_photo(peer=peer, photo_id=photo_id, reason=reason, message=message, wait=wait, timeout=timeout))

    def account_set_authorization_t_t_l(self, *, authorization_ttl_days: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_set_authorization_t_t_l(authorization_ttl_days=authorization_ttl_days, wait=wait, timeout=timeout))

    def account_change_authorization_settings(self, *, hash: Any, confirmed: Any=None, encrypted_requests_disabled: Any=None, call_requests_disabled: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_change_authorization_settings(hash=hash, confirmed=confirmed, encrypted_requests_disabled=encrypted_requests_disabled, call_requests_disabled=call_requests_disabled, wait=wait, timeout=timeout))

    def account_update_emoji_status(self, *, emoji_status: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_emoji_status(emoji_status=emoji_status, wait=wait, timeout=timeout))

    def account_get_recent_emoji_statuses(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_recent_emoji_statuses(hash=hash, wait=wait, timeout=timeout))

    def account_reorder_usernames(self, *, order: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_reorder_usernames(order=order, wait=wait, timeout=timeout))

    def account_toggle_username(self, *, username: Any, active: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_toggle_username(username=username, active=active, wait=wait, timeout=timeout))

    def account_update_gender(self, *, gender: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_gender(gender=gender, wait=wait, timeout=timeout))

    def account_update_user_location(self, *, geo_point: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_user_location(geo_point=geo_point, wait=wait, timeout=timeout))

    def users_get_users(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.users_get_users(id=id, wait=wait, timeout=timeout))

    def users_get_full_user(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.users_get_full_user(id=id, wait=wait, timeout=timeout))

    def conference_create_conference_call(self, *, version: Any, random_id: Any=None, name: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_create_conference_call(version=version, random_id=random_id, name=name, wait=wait, timeout=timeout))

    def conference_resolve_conference_call(self, *, slug: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_resolve_conference_call(slug=slug, wait=wait, timeout=timeout))

    def conference_get_conference_call(self, *, conference: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_get_conference_call(conference=conference, wait=wait, timeout=timeout))

    def conference_join_conference_call(self, *, version: Any, conference: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_join_conference_call(version=version, conference=conference, wait=wait, timeout=timeout))

    def conference_leave_conference_call(self, *, conference: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_leave_conference_call(conference=conference, wait=wait, timeout=timeout))

    def conference_discard_conference_call(self, *, conference: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_discard_conference_call(conference=conference, wait=wait, timeout=timeout))

    def conference_remove_conference_participant(self, *, conference: Any, participant: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_remove_conference_participant(conference=conference, participant=participant, wait=wait, timeout=timeout))

    def conference_ban_conference_participant(self, *, conference: Any, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_ban_conference_participant(conference=conference, peer=peer, wait=wait, timeout=timeout))

    def conference_unban_conference_participant(self, *, conference: Any, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_unban_conference_participant(conference=conference, peer=peer, wait=wait, timeout=timeout))

    def conference_get_banned_conference_participants(self, *, conference: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_get_banned_conference_participants(conference=conference, wait=wait, timeout=timeout))

    def conference_get_active_conference_calls(self, *, limit: Any, offset: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_get_active_conference_calls(limit=limit, offset=offset, wait=wait, timeout=timeout))

    def conference_mute_conference_participant(self, *, conference: Any, participant: Any, track: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_mute_conference_participant(conference=conference, participant=participant, track=track, wait=wait, timeout=timeout))

    def conference_set_conference_rating(self, *, conference: Any, rating: Any, comment: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.conference_set_conference_rating(conference=conference, rating=rating, comment=comment, wait=wait, timeout=timeout))

    def contacts_get_contacts(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_get_contacts(hash=hash, wait=wait, timeout=timeout))

    def contacts_import_contacts(self, *, contacts: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_import_contacts(contacts=contacts, wait=wait, timeout=timeout))

    def contacts_delete_contacts(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_delete_contacts(id=id, wait=wait, timeout=timeout))

    def contacts_block(self, *, id: Any, my_stories_from: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_block(id=id, my_stories_from=my_stories_from, wait=wait, timeout=timeout))

    def contacts_unblock(self, *, id: Any, my_stories_from: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_unblock(id=id, my_stories_from=my_stories_from, wait=wait, timeout=timeout))

    def contacts_get_blocked(self, *, offset: Any, limit: Any, my_stories_from: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_get_blocked(offset=offset, limit=limit, my_stories_from=my_stories_from, wait=wait, timeout=timeout))

    def contacts_search(self, *, q: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_search(q=q, limit=limit, wait=wait, timeout=timeout))

    def contacts_resolve_username(self, *, username: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_resolve_username(username=username, wait=wait, timeout=timeout))

    def contacts_get_top_peers(self, *, offset: Any, limit: Any, hash: Any, correspondents: Any=None, bots_pm: Any=None, bots_inline: Any=None, phone_calls: Any=None, forward_users: Any=None, forward_chats: Any=None, groups: Any=None, channels: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_get_top_peers(offset=offset, limit=limit, hash=hash, correspondents=correspondents, bots_pm=bots_pm, bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users, forward_chats=forward_chats, groups=groups, channels=channels, wait=wait, timeout=timeout))

    def contacts_add_contact(self, *, id: Any, first_name: Any, last_name: Any, phone: Any, add_phone_privacy_exception: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_add_contact(id=id, first_name=first_name, last_name=last_name, phone=phone, add_phone_privacy_exception=add_phone_privacy_exception, wait=wait, timeout=timeout))

    def contacts_resolve_phone(self, *, phone: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_resolve_phone(phone=phone, wait=wait, timeout=timeout))

    def contacts_edit_close_friends(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_edit_close_friends(id=id, wait=wait, timeout=timeout))

    def messages_get_messages(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_messages(id=id, wait=wait, timeout=timeout))

    def messages_get_dialogs(self, *, offset_date: Any, offset_id: Any, offset_peer: Any, limit: Any, hash: Any, exclude_pinned: Any=None, folder_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_dialogs(offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash, exclude_pinned=exclude_pinned, folder_id=folder_id, wait=wait, timeout=timeout))

    def messages_get_history(self, *, peer: Any, offset_id: Any, offset_date: Any, add_offset: Any, limit: Any, max_id: Any, min_id: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_history(peer=peer, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash, wait=wait, timeout=timeout))

    def messages_search(self, *, peer: Any, q: Any, filter: Any, min_date: Any, max_date: Any, offset_id: Any, add_offset: Any, limit: Any, max_id: Any, min_id: Any, hash: Any, from_id: Any=None, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_search(peer=peer, q=q, filter=filter, min_date=min_date, max_date=max_date, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash, from_id=from_id, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_read_history(self, *, peer: Any, max_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_read_history(peer=peer, max_id=max_id, wait=wait, timeout=timeout))

    def messages_delete_history(self, *, peer: Any, max_id: Any, just_clear: Any=None, revoke: Any=None, min_date: Any=None, max_date: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_history(peer=peer, max_id=max_id, just_clear=just_clear, revoke=revoke, min_date=min_date, max_date=max_date, wait=wait, timeout=timeout))

    def messages_delete_messages(self, *, id: Any, revoke: Any=None, peer: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_messages(id=id, revoke=revoke, peer=peer, wait=wait, timeout=timeout))

    def messages_received_messages(self, *, max_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_received_messages(max_id=max_id, wait=wait, timeout=timeout))

    def messages_set_typing(self, *, peer: Any, action: Any, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_set_typing(peer=peer, action=action, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_send_message(self, *, peer: Any, message: Any, no_webpage: Any=None, silent: Any=None, background: Any=None, clear_draft: Any=None, noforwards: Any=None, update_stickersets_order: Any=None, invert_media: Any=None, reply_to: Any=None, random_id: Any=None, reply_markup: Any=None, entities: Any=None, schedule_date: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_message(peer=peer, message=message, no_webpage=no_webpage, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, reply_to=reply_to, random_id=random_id, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, send_as=send_as, wait=wait, timeout=timeout))

    def messages_send_media(self, *, peer: Any, media: Any, message: Any, silent: Any=None, background: Any=None, clear_draft: Any=None, noforwards: Any=None, update_stickersets_order: Any=None, invert_media: Any=None, reply_to: Any=None, random_id: Any=None, reply_markup: Any=None, entities: Any=None, schedule_date: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_media(peer=peer, media=media, message=message, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, reply_to=reply_to, random_id=random_id, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, send_as=send_as, wait=wait, timeout=timeout))

    def messages_forward_messages(self, *, from_peer: Any, id: Any, to_peer: Any, silent: Any=None, background: Any=None, with_my_score: Any=None, drop_author: Any=None, drop_media_captions: Any=None, noforwards: Any=None, random_id: Any=None, top_msg_id: Any=None, schedule_date: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_forward_messages(from_peer=from_peer, id=id, to_peer=to_peer, silent=silent, background=background, with_my_score=with_my_score, drop_author=drop_author, drop_media_captions=drop_media_captions, noforwards=noforwards, random_id=random_id, top_msg_id=top_msg_id, schedule_date=schedule_date, send_as=send_as, wait=wait, timeout=timeout))

    def messages_report_spam(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_report_spam(peer=peer, wait=wait, timeout=timeout))

    def messages_get_peer_settings(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_peer_settings(peer=peer, wait=wait, timeout=timeout))

    def messages_report(self, *, peer: Any, id: Any, reason: Any, message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_report(peer=peer, id=id, reason=reason, message=message, wait=wait, timeout=timeout))

    def messages_get_chats(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_chats(id=id, wait=wait, timeout=timeout))

    def messages_get_full_chat(self, *, chat_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_full_chat(chat_id=chat_id, wait=wait, timeout=timeout))

    def messages_edit_chat_title(self, *, chat_id: Any, title: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_edit_chat_title(chat_id=chat_id, title=title, wait=wait, timeout=timeout))

    def messages_edit_chat_photo(self, *, chat_id: Any, photo: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_edit_chat_photo(chat_id=chat_id, photo=photo, wait=wait, timeout=timeout))

    def messages_add_chat_user(self, *, chat_id: Any, user_id: Any, fwd_limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_add_chat_user(chat_id=chat_id, user_id=user_id, fwd_limit=fwd_limit, wait=wait, timeout=timeout))

    def messages_delete_chat_user(self, *, chat_id: Any, user_id: Any, revoke_history: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_chat_user(chat_id=chat_id, user_id=user_id, revoke_history=revoke_history, wait=wait, timeout=timeout))

    def messages_create_chat(self, *, users: Any, title: Any, ttl_period: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_create_chat(users=users, title=title, ttl_period=ttl_period, wait=wait, timeout=timeout))

    def messages_get_dh_config(self, *, version: Any, random_length: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_dh_config(version=version, random_length=random_length, wait=wait, timeout=timeout))

    def messages_read_message_contents(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_read_message_contents(id=id, wait=wait, timeout=timeout))

    def messages_get_stickers(self, *, emoticon: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_stickers(emoticon=emoticon, hash=hash, wait=wait, timeout=timeout))

    def messages_get_all_stickers(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_all_stickers(hash=hash, wait=wait, timeout=timeout))

    def messages_get_web_page_preview(self, *, message: Any, entities: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_web_page_preview(message=message, entities=entities, wait=wait, timeout=timeout))

    def messages_export_chat_invite(self, *, peer: Any, legacy_revoke_permanent: Any=None, request_needed: Any=None, expire_date: Any=None, usage_limit: Any=None, title: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_export_chat_invite(peer=peer, legacy_revoke_permanent=legacy_revoke_permanent, request_needed=request_needed, expire_date=expire_date, usage_limit=usage_limit, title=title, wait=wait, timeout=timeout))

    def messages_check_chat_invite(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_check_chat_invite(hash=hash, wait=wait, timeout=timeout))

    def messages_import_chat_invite(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_import_chat_invite(hash=hash, wait=wait, timeout=timeout))

    def messages_get_sticker_set(self, *, stickerset: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_sticker_set(stickerset=stickerset, hash=hash, wait=wait, timeout=timeout))

    def messages_install_sticker_set(self, *, stickerset: Any, archived: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_install_sticker_set(stickerset=stickerset, archived=archived, wait=wait, timeout=timeout))

    def messages_uninstall_sticker_set(self, *, stickerset: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_uninstall_sticker_set(stickerset=stickerset, wait=wait, timeout=timeout))

    def messages_start_bot(self, *, bot: Any, peer: Any, start_param: Any, random_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_start_bot(bot=bot, peer=peer, start_param=start_param, random_id=random_id, wait=wait, timeout=timeout))

    def messages_get_messages_views(self, *, peer: Any, id: Any, increment: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_messages_views(peer=peer, id=id, increment=increment, wait=wait, timeout=timeout))

    def messages_migrate_chat(self, *, chat_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_migrate_chat(chat_id=chat_id, wait=wait, timeout=timeout))

    def messages_search_global(self, *, q: Any, filter: Any, min_date: Any, max_date: Any, offset_rate: Any, offset_peer: Any, offset_id: Any, limit: Any, folder_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_search_global(q=q, filter=filter, min_date=min_date, max_date=max_date, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit, folder_id=folder_id, wait=wait, timeout=timeout))

    def messages_get_document_by_hash(self, *, sha256: Any, size: Any, mime_type: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_document_by_hash(sha256=sha256, size=size, mime_type=mime_type, wait=wait, timeout=timeout))

    def messages_get_saved_gifs(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_saved_gifs(hash=hash, wait=wait, timeout=timeout))

    def messages_save_gif(self, *, id: Any, unsave: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_save_gif(id=id, unsave=unsave, wait=wait, timeout=timeout))

    def messages_get_inline_bot_results(self, *, bot: Any, peer: Any, query: Any, offset: Any, geo_point: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_inline_bot_results(bot=bot, peer=peer, query=query, offset=offset, geo_point=geo_point, wait=wait, timeout=timeout))

    def messages_send_inline_bot_result(self, *, peer: Any, query_id: Any, id: Any, silent: Any=None, background: Any=None, clear_draft: Any=None, hide_via: Any=None, reply_to: Any=None, random_id: Any=None, schedule_date: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_inline_bot_result(peer=peer, query_id=query_id, id=id, silent=silent, background=background, clear_draft=clear_draft, hide_via=hide_via, reply_to=reply_to, random_id=random_id, schedule_date=schedule_date, send_as=send_as, wait=wait, timeout=timeout))

    def messages_edit_message(self, *, peer: Any, id: Any, no_webpage: Any=None, invert_media: Any=None, message: Any=None, media: Any=None, reply_markup: Any=None, entities: Any=None, schedule_date: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_edit_message(peer=peer, id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, wait=wait, timeout=timeout))

    def messages_get_bot_callback_answer(self, *, peer: Any, msg_id: Any, game: Any=None, data: Any=None, password: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_bot_callback_answer(peer=peer, msg_id=msg_id, game=game, data=data, password=password, wait=wait, timeout=timeout))

    def messages_get_peer_dialogs(self, *, peers: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_peer_dialogs(peers=peers, wait=wait, timeout=timeout))

    def messages_save_draft(self, *, peer: Any, message: Any, no_webpage: Any=None, invert_media: Any=None, reply_to: Any=None, entities: Any=None, media: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_save_draft(peer=peer, message=message, no_webpage=no_webpage, invert_media=invert_media, reply_to=reply_to, entities=entities, media=media, wait=wait, timeout=timeout))

    def messages_get_featured_stickers(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_featured_stickers(hash=hash, wait=wait, timeout=timeout))

    def messages_read_featured_stickers(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_read_featured_stickers(id=id, wait=wait, timeout=timeout))

    def messages_get_recent_stickers(self, *, hash: Any, attached: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_recent_stickers(hash=hash, attached=attached, wait=wait, timeout=timeout))

    def messages_save_recent_sticker(self, *, id: Any, unsave: Any, attached: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_save_recent_sticker(id=id, unsave=unsave, attached=attached, wait=wait, timeout=timeout))

    def messages_clear_recent_stickers(self, *, attached: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_clear_recent_stickers(attached=attached, wait=wait, timeout=timeout))

    def messages_get_archived_stickers(self, *, offset_id: Any, limit: Any, masks: Any=None, emojis: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_archived_stickers(offset_id=offset_id, limit=limit, masks=masks, emojis=emojis, wait=wait, timeout=timeout))

    def messages_get_common_chats(self, *, user_id: Any, max_id: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_common_chats(user_id=user_id, max_id=max_id, limit=limit, wait=wait, timeout=timeout))

    def messages_get_web_page(self, *, url: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_web_page(url=url, hash=hash, wait=wait, timeout=timeout))

    def messages_toggle_dialog_pin(self, *, peer: Any, pinned: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_toggle_dialog_pin(peer=peer, pinned=pinned, wait=wait, timeout=timeout))

    def messages_get_pinned_dialogs(self, *, folder_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_pinned_dialogs(folder_id=folder_id, wait=wait, timeout=timeout))

    def messages_upload_media(self, *, peer: Any, media: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_upload_media(peer=peer, media=media, wait=wait, timeout=timeout))

    def messages_get_faved_stickers(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_faved_stickers(hash=hash, wait=wait, timeout=timeout))

    def messages_fave_sticker(self, *, id: Any, unfave: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_fave_sticker(id=id, unfave=unfave, wait=wait, timeout=timeout))

    def messages_get_unread_mentions(self, *, peer: Any, offset_id: Any, add_offset: Any, limit: Any, max_id: Any, min_id: Any, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_unread_mentions(peer=peer, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_read_mentions(self, *, peer: Any, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_read_mentions(peer=peer, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_send_multi_media(self, *, peer: Any, multi_media: Any, silent: Any=None, background: Any=None, clear_draft: Any=None, noforwards: Any=None, update_stickersets_order: Any=None, invert_media: Any=None, reply_to: Any=None, schedule_date: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_multi_media(peer=peer, multi_media=multi_media, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, reply_to=reply_to, schedule_date=schedule_date, send_as=send_as, wait=wait, timeout=timeout))

    def messages_search_sticker_sets(self, *, q: Any, hash: Any, exclude_featured: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_search_sticker_sets(q=q, hash=hash, exclude_featured=exclude_featured, wait=wait, timeout=timeout))

    def messages_mark_dialog_unread(self, *, peer: Any, unread: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_mark_dialog_unread(peer=peer, unread=unread, wait=wait, timeout=timeout))

    def messages_update_pinned_message(self, *, peer: Any, id: Any, silent: Any=None, unpin: Any=None, pm_oneside: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_update_pinned_message(peer=peer, id=id, silent=silent, unpin=unpin, pm_oneside=pm_oneside, wait=wait, timeout=timeout))

    def messages_send_vote(self, *, peer: Any, msg_id: Any, options: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_vote(peer=peer, msg_id=msg_id, options=options, wait=wait, timeout=timeout))

    def messages_get_poll_results(self, *, peer: Any, msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_poll_results(peer=peer, msg_id=msg_id, wait=wait, timeout=timeout))

    def messages_get_onlines(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_onlines(peer=peer, wait=wait, timeout=timeout))

    def messages_edit_chat_about(self, *, peer: Any, about: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_edit_chat_about(peer=peer, about=about, wait=wait, timeout=timeout))

    def messages_edit_chat_default_banned_rights(self, *, peer: Any, banned_rights: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_edit_chat_default_banned_rights(peer=peer, banned_rights=banned_rights, wait=wait, timeout=timeout))

    def messages_get_emoji_keywords_difference(self, *, lang_code: Any, from_version: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_emoji_keywords_difference(lang_code=lang_code, from_version=from_version, wait=wait, timeout=timeout))

    def messages_request_url_auth(self, *, peer: Any=None, msg_id: Any=None, button_id: Any=None, url: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_request_url_auth(peer=peer, msg_id=msg_id, button_id=button_id, url=url, wait=wait, timeout=timeout))

    def messages_accept_url_auth(self, *, write_allowed: Any=None, peer: Any=None, msg_id: Any=None, button_id: Any=None, url: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_accept_url_auth(write_allowed=write_allowed, peer=peer, msg_id=msg_id, button_id=button_id, url=url, wait=wait, timeout=timeout))

    def messages_hide_peer_settings_bar(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_hide_peer_settings_bar(peer=peer, wait=wait, timeout=timeout))

    def messages_get_scheduled_history(self, *, peer: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_scheduled_history(peer=peer, hash=hash, wait=wait, timeout=timeout))

    def messages_send_scheduled_messages(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_scheduled_messages(peer=peer, id=id, wait=wait, timeout=timeout))

    def messages_delete_scheduled_messages(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_scheduled_messages(peer=peer, id=id, wait=wait, timeout=timeout))

    def messages_get_poll_votes(self, *, peer: Any, id: Any, limit: Any, option: Any=None, offset: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_poll_votes(peer=peer, id=id, limit=limit, option=option, offset=offset, wait=wait, timeout=timeout))

    def messages_get_dialog_filters(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_dialog_filters(wait=wait, timeout=timeout))

    def messages_get_suggested_dialog_filters(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_suggested_dialog_filters(wait=wait, timeout=timeout))

    def messages_update_dialog_filter(self, *, id: Any, filter: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_update_dialog_filter(id=id, filter=filter, wait=wait, timeout=timeout))

    def messages_update_dialog_filters_order(self, *, order: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_update_dialog_filters_order(order=order, wait=wait, timeout=timeout))

    def messages_get_replies(self, *, peer: Any, msg_id: Any, offset_id: Any, offset_date: Any, add_offset: Any, limit: Any, max_id: Any, min_id: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_replies(peer=peer, msg_id=msg_id, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash, wait=wait, timeout=timeout))

    def messages_get_discussion_message(self, *, peer: Any, msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_discussion_message(peer=peer, msg_id=msg_id, wait=wait, timeout=timeout))

    def messages_read_discussion(self, *, peer: Any, msg_id: Any, read_max_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_read_discussion(peer=peer, msg_id=msg_id, read_max_id=read_max_id, wait=wait, timeout=timeout))

    def messages_unpin_all_messages(self, *, peer: Any, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_unpin_all_messages(peer=peer, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_delete_chat(self, *, chat_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_chat(chat_id=chat_id, wait=wait, timeout=timeout))

    def messages_get_exported_chat_invites(self, *, peer: Any, admin_id: Any, limit: Any, revoked: Any=None, offset_date: Any=None, offset_link: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_exported_chat_invites(peer=peer, admin_id=admin_id, limit=limit, revoked=revoked, offset_date=offset_date, offset_link=offset_link, wait=wait, timeout=timeout))

    def messages_edit_exported_chat_invite(self, *, peer: Any, link: Any, revoked: Any=None, expire_date: Any=None, usage_limit: Any=None, request_needed: Any=None, title: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_edit_exported_chat_invite(peer=peer, link=link, revoked=revoked, expire_date=expire_date, usage_limit=usage_limit, request_needed=request_needed, title=title, wait=wait, timeout=timeout))

    def messages_delete_revoked_exported_chat_invites(self, *, peer: Any, admin_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_revoked_exported_chat_invites(peer=peer, admin_id=admin_id, wait=wait, timeout=timeout))

    def messages_delete_exported_chat_invite(self, *, peer: Any, link: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_delete_exported_chat_invite(peer=peer, link=link, wait=wait, timeout=timeout))

    def messages_get_chat_invite_importers(self, *, peer: Any, offset_date: Any, offset_user: Any, limit: Any, requested: Any=None, link: Any=None, q: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_chat_invite_importers(peer=peer, offset_date=offset_date, offset_user=offset_user, limit=limit, requested=requested, link=link, q=q, wait=wait, timeout=timeout))

    def messages_get_message_read_participants(self, *, peer: Any, msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_message_read_participants(peer=peer, msg_id=msg_id, wait=wait, timeout=timeout))

    def messages_hide_chat_join_request(self, *, peer: Any, user_id: Any, approved: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_hide_chat_join_request(peer=peer, user_id=user_id, approved=approved, wait=wait, timeout=timeout))

    def messages_hide_all_chat_join_requests(self, *, peer: Any, approved: Any=None, link: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_hide_all_chat_join_requests(peer=peer, approved=approved, link=link, wait=wait, timeout=timeout))

    def messages_toggle_no_forwards(self, *, peer: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_toggle_no_forwards(peer=peer, enabled=enabled, wait=wait, timeout=timeout))

    def messages_save_default_send_as(self, *, peer: Any, send_as: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_save_default_send_as(peer=peer, send_as=send_as, wait=wait, timeout=timeout))

    def messages_send_reaction(self, *, peer: Any, msg_id: Any, big: Any=None, add_to_recent: Any=None, reaction: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_reaction(peer=peer, msg_id=msg_id, big=big, add_to_recent=add_to_recent, reaction=reaction, wait=wait, timeout=timeout))

    def messages_get_messages_reactions(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_messages_reactions(peer=peer, id=id, wait=wait, timeout=timeout))

    def messages_get_message_reactions_list(self, *, peer: Any, id: Any, limit: Any, reaction: Any=None, offset: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_message_reactions_list(peer=peer, id=id, limit=limit, reaction=reaction, offset=offset, wait=wait, timeout=timeout))

    def messages_set_chat_available_reactions(self, *, peer: Any, available_reactions: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_set_chat_available_reactions(peer=peer, available_reactions=available_reactions, wait=wait, timeout=timeout))

    def messages_get_available_reactions(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_available_reactions(hash=hash, wait=wait, timeout=timeout))

    def messages_set_default_reaction(self, *, reaction: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_set_default_reaction(reaction=reaction, wait=wait, timeout=timeout))

    def messages_translate_text(self, *, to_lang: Any, peer: Any=None, id: Any=None, text: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_translate_text(to_lang=to_lang, peer=peer, id=id, text=text, wait=wait, timeout=timeout))

    def messages_get_unread_reactions(self, *, peer: Any, offset_id: Any, add_offset: Any, limit: Any, max_id: Any, min_id: Any, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_unread_reactions(peer=peer, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_read_reactions(self, *, peer: Any, top_msg_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_read_reactions(peer=peer, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def messages_get_attach_menu_bots(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_attach_menu_bots(hash=hash, wait=wait, timeout=timeout))

    def messages_get_attach_menu_bot(self, *, bot: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_attach_menu_bot(bot=bot, wait=wait, timeout=timeout))

    def messages_toggle_bot_in_attach_menu(self, *, bot: Any, enabled: Any, write_allowed: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_toggle_bot_in_attach_menu(bot=bot, enabled=enabled, write_allowed=write_allowed, wait=wait, timeout=timeout))

    def messages_request_web_view(self, *, peer: Any, bot: Any, platform: Any, from_bot_menu: Any=None, silent: Any=None, url: Any=None, start_param: Any=None, theme_params: Any=None, reply_to: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_request_web_view(peer=peer, bot=bot, platform=platform, from_bot_menu=from_bot_menu, silent=silent, url=url, start_param=start_param, theme_params=theme_params, reply_to=reply_to, send_as=send_as, wait=wait, timeout=timeout))

    def messages_prolong_web_view(self, *, peer: Any, bot: Any, query_id: Any, silent: Any=None, reply_to: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_prolong_web_view(peer=peer, bot=bot, query_id=query_id, silent=silent, reply_to=reply_to, send_as=send_as, wait=wait, timeout=timeout))

    def messages_request_simple_web_view(self, *, bot: Any, platform: Any, from_switch_webview: Any=None, from_side_menu: Any=None, url: Any=None, start_param: Any=None, theme_params: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_request_simple_web_view(bot=bot, platform=platform, from_switch_webview=from_switch_webview, from_side_menu=from_side_menu, url=url, start_param=start_param, theme_params=theme_params, wait=wait, timeout=timeout))

    def messages_send_web_view_result_message(self, *, bot_query_id: Any, result: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_web_view_result_message(bot_query_id=bot_query_id, result=result, wait=wait, timeout=timeout))

    def messages_send_web_view_data(self, *, bot: Any, button_text: Any, data: Any, random_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_send_web_view_data(bot=bot, button_text=button_text, data=data, random_id=random_id, wait=wait, timeout=timeout))

    def messages_transcribe_audio(self, *, peer: Any, msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_transcribe_audio(peer=peer, msg_id=msg_id, wait=wait, timeout=timeout))

    def messages_get_custom_emoji_documents(self, *, document_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_custom_emoji_documents(document_id=document_id, wait=wait, timeout=timeout))

    def messages_get_emoji_stickers(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_emoji_stickers(hash=hash, wait=wait, timeout=timeout))

    def messages_get_featured_emoji_stickers(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_featured_emoji_stickers(hash=hash, wait=wait, timeout=timeout))

    def messages_get_top_reactions(self, *, limit: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_top_reactions(limit=limit, hash=hash, wait=wait, timeout=timeout))

    def messages_get_recent_reactions(self, *, limit: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_recent_reactions(limit=limit, hash=hash, wait=wait, timeout=timeout))

    def messages_clear_recent_reactions(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_clear_recent_reactions(wait=wait, timeout=timeout))

    def messages_get_extended_media(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_extended_media(peer=peer, id=id, wait=wait, timeout=timeout))

    def messages_toggle_peer_translations(self, *, peer: Any, disabled: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_toggle_peer_translations(peer=peer, disabled=disabled, wait=wait, timeout=timeout))

    def messages_get_bot_app(self, *, app: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_get_bot_app(app=app, hash=hash, wait=wait, timeout=timeout))

    def messages_request_app_web_view(self, *, peer: Any, app: Any, platform: Any, write_allowed: Any=None, start_param: Any=None, theme_params: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_request_app_web_view(peer=peer, app=app, platform=platform, write_allowed=write_allowed, start_param=start_param, theme_params=theme_params, wait=wait, timeout=timeout))

    def updates_get_state(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.updates_get_state(wait=wait, timeout=timeout))

    def updates_get_difference(self, *, pts: Any, date: Any, qts: Any, pts_limit: Any=None, pts_total_limit: Any=None, qts_limit: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.updates_get_difference(pts=pts, date=date, qts=qts, pts_limit=pts_limit, pts_total_limit=pts_total_limit, qts_limit=qts_limit, wait=wait, timeout=timeout))

    def updates_get_channel_difference(self, *, channel: Any, filter: Any, pts: Any, limit: Any, force: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.updates_get_channel_difference(channel=channel, filter=filter, pts=pts, limit=limit, force=force, wait=wait, timeout=timeout))

    def photos_update_profile_photo(self, *, id: Any, fallback: Any=None, bot: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.photos_update_profile_photo(id=id, fallback=fallback, bot=bot, wait=wait, timeout=timeout))

    def photos_upload_profile_photo(self, *, fallback: Any=None, bot: Any=None, file: Any=None, video: Any=None, video_start_ts: Any=None, video_emoji_markup: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.photos_upload_profile_photo(fallback=fallback, bot=bot, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup, wait=wait, timeout=timeout))

    def photos_delete_photos(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.photos_delete_photos(id=id, wait=wait, timeout=timeout))

    def photos_get_user_photos(self, *, user_id: Any, offset: Any, max_id: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.photos_get_user_photos(user_id=user_id, offset=offset, max_id=max_id, limit=limit, wait=wait, timeout=timeout))

    def photos_upload_contact_profile_photo(self, *, user_id: Any, suggest: Any=None, save: Any=None, file: Any=None, video: Any=None, video_start_ts: Any=None, video_emoji_markup: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.photos_upload_contact_profile_photo(user_id=user_id, suggest=suggest, save=save, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup, wait=wait, timeout=timeout))

    def upload_save_file_part(self, *, file_id: Any, file_part: Any, bytes: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.upload_save_file_part(file_id=file_id, file_part=file_part, bytes=bytes, wait=wait, timeout=timeout))

    def upload_get_file(self, *, location: Any, offset: Any, limit: Any, precise: Any=None, cdn_supported: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.upload_get_file(location=location, offset=offset, limit=limit, precise=precise, cdn_supported=cdn_supported, wait=wait, timeout=timeout))

    def upload_save_big_file_part(self, *, file_id: Any, file_part: Any, file_total_parts: Any, bytes: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.upload_save_big_file_part(file_id=file_id, file_part=file_part, file_total_parts=file_total_parts, bytes=bytes, wait=wait, timeout=timeout))

    def upload_get_web_file(self, *, location: Any, offset: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.upload_get_web_file(location=location, offset=offset, limit=limit, wait=wait, timeout=timeout))

    def help_get_config(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_config(wait=wait, timeout=timeout))

    def help_get_nearest_dc(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_nearest_dc(wait=wait, timeout=timeout))

    def help_get_support(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_support(wait=wait, timeout=timeout))

    def help_accept_terms_of_service(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_accept_terms_of_service(id=id, wait=wait, timeout=timeout))

    def help_get_app_config(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_app_config(hash=hash, wait=wait, timeout=timeout))

    def help_get_countries_list(self, *, lang_code: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_countries_list(lang_code=lang_code, hash=hash, wait=wait, timeout=timeout))

    def help_get_premium_promo(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_premium_promo(wait=wait, timeout=timeout))

    def help_get_peer_colors(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_peer_colors(hash=hash, wait=wait, timeout=timeout))

    def help_get_peer_profile_colors(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_peer_profile_colors(hash=hash, wait=wait, timeout=timeout))

    def channels_read_history(self, *, channel: Any, max_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_read_history(channel=channel, max_id=max_id, wait=wait, timeout=timeout))

    def channels_delete_messages(self, *, channel: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_delete_messages(channel=channel, id=id, wait=wait, timeout=timeout))

    def channels_get_messages(self, *, channel: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_messages(channel=channel, id=id, wait=wait, timeout=timeout))

    def channels_get_participants(self, *, channel: Any, filter: Any, offset: Any, limit: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_participants(channel=channel, filter=filter, offset=offset, limit=limit, hash=hash, wait=wait, timeout=timeout))

    def channels_get_participant(self, *, channel: Any, participant: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_participant(channel=channel, participant=participant, wait=wait, timeout=timeout))

    def channels_get_channels(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_channels(id=id, wait=wait, timeout=timeout))

    def channels_get_full_channel(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_full_channel(channel=channel, wait=wait, timeout=timeout))

    def channels_create_channel(self, *, title: Any, about: Any, broadcast: Any=None, megagroup: Any=None, for_import: Any=None, forum: Any=None, geo_point: Any=None, address: Any=None, ttl_period: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_create_channel(title=title, about=about, broadcast=broadcast, megagroup=megagroup, for_import=for_import, forum=forum, geo_point=geo_point, address=address, ttl_period=ttl_period, wait=wait, timeout=timeout))

    def channels_edit_admin(self, *, channel: Any, user_id: Any, admin_rights: Any, rank: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_edit_admin(channel=channel, user_id=user_id, admin_rights=admin_rights, rank=rank, wait=wait, timeout=timeout))

    def channels_edit_title(self, *, channel: Any, title: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_edit_title(channel=channel, title=title, wait=wait, timeout=timeout))

    def channels_edit_photo(self, *, channel: Any, photo: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_edit_photo(channel=channel, photo=photo, wait=wait, timeout=timeout))

    def channels_check_username(self, *, channel: Any, username: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_check_username(channel=channel, username=username, wait=wait, timeout=timeout))

    def channels_update_username(self, *, channel: Any, username: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_update_username(channel=channel, username=username, wait=wait, timeout=timeout))

    def channels_join_channel(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_join_channel(channel=channel, wait=wait, timeout=timeout))

    def channels_leave_channel(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_leave_channel(channel=channel, wait=wait, timeout=timeout))

    def channels_invite_to_channel(self, *, channel: Any, users: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_invite_to_channel(channel=channel, users=users, wait=wait, timeout=timeout))

    def channels_delete_channel(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_delete_channel(channel=channel, wait=wait, timeout=timeout))

    def channels_toggle_signatures(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_signatures(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_get_admined_public_channels(self, *, by_location: Any=None, check_limit: Any=None, for_personal: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_admined_public_channels(by_location=by_location, check_limit=check_limit, for_personal=for_personal, wait=wait, timeout=timeout))

    def channels_edit_banned(self, *, channel: Any, participant: Any, banned_rights: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_edit_banned(channel=channel, participant=participant, banned_rights=banned_rights, wait=wait, timeout=timeout))

    def channels_read_message_contents(self, *, channel: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_read_message_contents(channel=channel, id=id, wait=wait, timeout=timeout))

    def channels_toggle_pre_history_hidden(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_pre_history_hidden(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_get_groups_for_discussion(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_groups_for_discussion(wait=wait, timeout=timeout))

    def channels_set_discussion_group(self, *, broadcast: Any, group: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_set_discussion_group(broadcast=broadcast, group=group, wait=wait, timeout=timeout))

    def channels_view_sponsored_message(self, *, channel: Any, random_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_view_sponsored_message(channel=channel, random_id=random_id, wait=wait, timeout=timeout))

    def channels_get_sponsored_messages(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_sponsored_messages(channel=channel, wait=wait, timeout=timeout))

    def channels_get_send_as(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_send_as(peer=peer, wait=wait, timeout=timeout))

    def channels_toggle_join_to_send(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_join_to_send(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_toggle_join_request(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_join_request(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_reorder_usernames(self, *, channel: Any, order: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_reorder_usernames(channel=channel, order=order, wait=wait, timeout=timeout))

    def channels_toggle_username(self, *, channel: Any, username: Any, active: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_username(channel=channel, username=username, active=active, wait=wait, timeout=timeout))

    def channels_deactivate_all_usernames(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_deactivate_all_usernames(channel=channel, wait=wait, timeout=timeout))

    def channels_toggle_forum(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_forum(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_create_forum_topic(self, *, channel: Any, title: Any, icon_color: Any=None, icon_emoji_id: Any=None, random_id: Any=None, send_as: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_create_forum_topic(channel=channel, title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id, random_id=random_id, send_as=send_as, wait=wait, timeout=timeout))

    def channels_get_forum_topics(self, *, channel: Any, offset_date: Any, offset_id: Any, offset_topic: Any, limit: Any, q: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_forum_topics(channel=channel, offset_date=offset_date, offset_id=offset_id, offset_topic=offset_topic, limit=limit, q=q, wait=wait, timeout=timeout))

    def channels_get_forum_topics_by_i_d(self, *, channel: Any, topics: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_get_forum_topics_by_i_d(channel=channel, topics=topics, wait=wait, timeout=timeout))

    def channels_edit_forum_topic(self, *, channel: Any, topic_id: Any, title: Any=None, icon_emoji_id: Any=None, closed: Any=None, hidden: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_edit_forum_topic(channel=channel, topic_id=topic_id, title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden, wait=wait, timeout=timeout))

    def channels_update_pinned_forum_topic(self, *, channel: Any, topic_id: Any, pinned: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_update_pinned_forum_topic(channel=channel, topic_id=topic_id, pinned=pinned, wait=wait, timeout=timeout))

    def channels_delete_topic_history(self, *, channel: Any, top_msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_delete_topic_history(channel=channel, top_msg_id=top_msg_id, wait=wait, timeout=timeout))

    def channels_toggle_participants_hidden(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_participants_hidden(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_click_sponsored_message(self, *, channel: Any, random_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_click_sponsored_message(channel=channel, random_id=random_id, wait=wait, timeout=timeout))

    def channels_toggle_view_forum_as_messages(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_view_forum_as_messages(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def channels_toggle_membership_message_visibility(self, *, channel: Any, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.channels_toggle_membership_message_visibility(channel=channel, enabled=enabled, wait=wait, timeout=timeout))

    def bots_can_send_message(self, *, bot: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.bots_can_send_message(bot=bot, wait=wait, timeout=timeout))

    def bots_allow_send_message(self, *, bot: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.bots_allow_send_message(bot=bot, wait=wait, timeout=timeout))

    def bots_invoke_web_view_custom_method(self, *, bot: Any, custom_method: Any, params: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.bots_invoke_web_view_custom_method(bot=bot, custom_method=custom_method, params=params, wait=wait, timeout=timeout))

    def payments_get_payment_form(self, *, invoice: Any, theme_params: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_get_payment_form(invoice=invoice, theme_params=theme_params, wait=wait, timeout=timeout))

    def payments_get_payment_receipt(self, *, peer: Any, msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_get_payment_receipt(peer=peer, msg_id=msg_id, wait=wait, timeout=timeout))

    def payments_validate_requested_info(self, *, invoice: Any, info: Any, save: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_validate_requested_info(invoice=invoice, info=info, save=save, wait=wait, timeout=timeout))

    def payments_send_payment_form(self, *, form_id: Any, invoice: Any, credentials: Any, requested_info_id: Any=None, shipping_option_id: Any=None, tip_amount: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_send_payment_form(form_id=form_id, invoice=invoice, credentials=credentials, requested_info_id=requested_info_id, shipping_option_id=shipping_option_id, tip_amount=tip_amount, wait=wait, timeout=timeout))

    def payments_get_saved_info(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_get_saved_info(wait=wait, timeout=timeout))

    def payments_check_gift_code(self, *, slug: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_check_gift_code(slug=slug, wait=wait, timeout=timeout))

    def payments_apply_gift_code(self, *, slug: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_apply_gift_code(slug=slug, wait=wait, timeout=timeout))

    def payments_get_giveaway_info(self, *, peer: Any, msg_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.payments_get_giveaway_info(peer=peer, msg_id=msg_id, wait=wait, timeout=timeout))

    def phone_request_call(self, *, user_id: Any, g_a_hash: Any, protocol: Any, video: Any=None, random_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_request_call(user_id=user_id, g_a_hash=g_a_hash, protocol=protocol, video=video, random_id=random_id, wait=wait, timeout=timeout))

    def phone_accept_call(self, *, peer: Any, g_b: Any, protocol: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_accept_call(peer=peer, g_b=g_b, protocol=protocol, wait=wait, timeout=timeout))

    def phone_confirm_call(self, *, peer: Any, g_a: Any, key_fingerprint: Any, protocol: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_confirm_call(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol, wait=wait, timeout=timeout))

    def phone_received_call(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_received_call(peer=peer, wait=wait, timeout=timeout))

    def phone_discard_call(self, *, peer: Any, duration: Any, reason: Any, connection_id: Any, video: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_discard_call(peer=peer, duration=duration, reason=reason, connection_id=connection_id, video=video, wait=wait, timeout=timeout))

    def phone_set_call_rating(self, *, peer: Any, rating: Any, comment: Any, user_initiative: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_set_call_rating(peer=peer, rating=rating, comment=comment, user_initiative=user_initiative, wait=wait, timeout=timeout))

    def phone_save_call_debug(self, *, peer: Any, debug: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_save_call_debug(peer=peer, debug=debug, wait=wait, timeout=timeout))

    def phone_send_signaling_data(self, *, peer: Any, data: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_send_signaling_data(peer=peer, data=data, wait=wait, timeout=timeout))

    def phone_create_group_call(self, *, peer: Any, rtmp_stream: Any=None, random_id: Any=None, title: Any=None, schedule_date: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_create_group_call(peer=peer, rtmp_stream=rtmp_stream, random_id=random_id, title=title, schedule_date=schedule_date, wait=wait, timeout=timeout))

    def phone_join_group_call(self, *, call: Any, join_as: Any, params: Any, muted: Any=None, video_stopped: Any=None, invite_hash: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_join_group_call(call=call, join_as=join_as, params=params, muted=muted, video_stopped=video_stopped, invite_hash=invite_hash, wait=wait, timeout=timeout))

    def phone_leave_group_call(self, *, call: Any, source: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_leave_group_call(call=call, source=source, wait=wait, timeout=timeout))

    def phone_discard_group_call(self, *, call: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_discard_group_call(call=call, wait=wait, timeout=timeout))

    def phone_get_group_call(self, *, call: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_get_group_call(call=call, limit=limit, wait=wait, timeout=timeout))

    def phone_get_group_participants(self, *, call: Any, ids: Any, sources: Any, offset: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_get_group_participants(call=call, ids=ids, sources=sources, offset=offset, limit=limit, wait=wait, timeout=timeout))

    def phone_edit_group_call_participant(self, *, call: Any, participant: Any, muted: Any=None, volume: Any=None, raise_hand: Any=None, video_stopped: Any=None, video_paused: Any=None, presentation_paused: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_edit_group_call_participant(call=call, participant=participant, muted=muted, volume=volume, raise_hand=raise_hand, video_stopped=video_stopped, video_paused=video_paused, presentation_paused=presentation_paused, wait=wait, timeout=timeout))

    def phone_export_group_call_invite(self, *, call: Any, can_self_unmute: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_export_group_call_invite(call=call, can_self_unmute=can_self_unmute, wait=wait, timeout=timeout))

    def phone_toggle_group_call_start_subscription(self, *, call: Any, subscribed: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_toggle_group_call_start_subscription(call=call, subscribed=subscribed, wait=wait, timeout=timeout))

    def phone_join_group_call_presentation(self, *, call: Any, params: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_join_group_call_presentation(call=call, params=params, wait=wait, timeout=timeout))

    def phone_leave_group_call_presentation(self, *, call: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.phone_leave_group_call_presentation(call=call, wait=wait, timeout=timeout))

    def langpack_get_lang_pack(self, *, lang_pack: Any, lang_code: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.langpack_get_lang_pack(lang_pack=lang_pack, lang_code=lang_code, wait=wait, timeout=timeout))

    def langpack_get_strings(self, *, lang_pack: Any, lang_code: Any, keys: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.langpack_get_strings(lang_pack=lang_pack, lang_code=lang_code, keys=keys, wait=wait, timeout=timeout))

    def langpack_get_difference(self, *, lang_pack: Any, lang_code: Any, from_version: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.langpack_get_difference(lang_pack=lang_pack, lang_code=lang_code, from_version=from_version, wait=wait, timeout=timeout))

    def langpack_get_languages(self, *, lang_pack: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.langpack_get_languages(lang_pack=lang_pack, wait=wait, timeout=timeout))

    def folders_edit_peer_folders(self, *, folder_peers: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.folders_edit_peer_folders(folder_peers=folder_peers, wait=wait, timeout=timeout))

    def stats_get_broadcast_stats(self, *, channel: Any, dark: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_get_broadcast_stats(channel=channel, dark=dark, wait=wait, timeout=timeout))

    def stats_load_async_graph(self, *, token: Any, x: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_load_async_graph(token=token, x=x, wait=wait, timeout=timeout))

    def stats_get_megagroup_stats(self, *, channel: Any, dark: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_get_megagroup_stats(channel=channel, dark=dark, wait=wait, timeout=timeout))

    def stats_get_message_public_forwards(self, *, channel: Any, msg_id: Any, offset_rate: Any, offset_peer: Any, offset_id: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_get_message_public_forwards(channel=channel, msg_id=msg_id, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit, wait=wait, timeout=timeout))

    def stats_get_message_stats(self, *, channel: Any, msg_id: Any, dark: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_get_message_stats(channel=channel, msg_id=msg_id, dark=dark, wait=wait, timeout=timeout))

    def stats_get_story_stats(self, *, peer: Any, id: Any, dark: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_get_story_stats(peer=peer, id=id, dark=dark, wait=wait, timeout=timeout))

    def stats_get_story_public_forwards(self, *, peer: Any, id: Any, offset: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stats_get_story_public_forwards(peer=peer, id=id, offset=offset, limit=limit, wait=wait, timeout=timeout))

    def chatlists_export_chatlist_invite(self, *, chatlist: Any, title: Any, peers: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_export_chatlist_invite(chatlist=chatlist, title=title, peers=peers, wait=wait, timeout=timeout))

    def chatlists_delete_exported_invite(self, *, chatlist: Any, slug: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_delete_exported_invite(chatlist=chatlist, slug=slug, wait=wait, timeout=timeout))

    def chatlists_edit_exported_invite(self, *, chatlist: Any, slug: Any, title: Any=None, peers: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_edit_exported_invite(chatlist=chatlist, slug=slug, title=title, peers=peers, wait=wait, timeout=timeout))

    def chatlists_get_exported_invites(self, *, chatlist: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_get_exported_invites(chatlist=chatlist, wait=wait, timeout=timeout))

    def chatlists_check_chatlist_invite(self, *, slug: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_check_chatlist_invite(slug=slug, wait=wait, timeout=timeout))

    def chatlists_join_chatlist_invite(self, *, slug: Any, peers: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_join_chatlist_invite(slug=slug, peers=peers, wait=wait, timeout=timeout))

    def chatlists_get_leave_chatlist_suggestions(self, *, chatlist: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_get_leave_chatlist_suggestions(chatlist=chatlist, wait=wait, timeout=timeout))

    def chatlists_leave_chatlist(self, *, chatlist: Any, peers: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.chatlists_leave_chatlist(chatlist=chatlist, peers=peers, wait=wait, timeout=timeout))

    def stories_edit_story(self, *, peer: Any, id: Any, media: Any=None, media_areas: Any=None, caption: Any=None, entities: Any=None, privacy_rules: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_edit_story(peer=peer, id=id, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules, wait=wait, timeout=timeout))

    def stories_delete_stories(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_delete_stories(peer=peer, id=id, wait=wait, timeout=timeout))

    def stories_toggle_pinned(self, *, peer: Any, id: Any, pinned: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_toggle_pinned(peer=peer, id=id, pinned=pinned, wait=wait, timeout=timeout))

    def stories_get_all_stories(self, *, next: Any=None, hidden: Any=None, state: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_all_stories(next=next, hidden=hidden, state=state, wait=wait, timeout=timeout))

    def stories_get_pinned_stories(self, *, peer: Any, offset_id: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_pinned_stories(peer=peer, offset_id=offset_id, limit=limit, wait=wait, timeout=timeout))

    def stories_get_stories_archive(self, *, peer: Any, offset_id: Any, limit: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_stories_archive(peer=peer, offset_id=offset_id, limit=limit, wait=wait, timeout=timeout))

    def stories_get_stories_by_i_d(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_stories_by_i_d(peer=peer, id=id, wait=wait, timeout=timeout))

    def stories_read_stories(self, *, peer: Any, max_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_read_stories(peer=peer, max_id=max_id, wait=wait, timeout=timeout))

    def stories_increment_story_views(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_increment_story_views(peer=peer, id=id, wait=wait, timeout=timeout))

    def stories_get_story_views_list(self, *, peer: Any, id: Any, offset: Any, limit: Any, just_contacts: Any=None, reactions_first: Any=None, q: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_story_views_list(peer=peer, id=id, offset=offset, limit=limit, just_contacts=just_contacts, reactions_first=reactions_first, q=q, wait=wait, timeout=timeout))

    def stories_export_story_link(self, *, peer: Any, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_export_story_link(peer=peer, id=id, wait=wait, timeout=timeout))

    def stories_report(self, *, peer: Any, id: Any, reason: Any, message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_report(peer=peer, id=id, reason=reason, message=message, wait=wait, timeout=timeout))

    def stories_activate_stealth_mode(self, *, past: Any=None, future: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_activate_stealth_mode(past=past, future=future, wait=wait, timeout=timeout))

    def stories_send_reaction(self, *, peer: Any, story_id: Any, reaction: Any, add_to_recent: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_send_reaction(peer=peer, story_id=story_id, reaction=reaction, add_to_recent=add_to_recent, wait=wait, timeout=timeout))

    def stories_get_peer_stories(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_peer_stories(peer=peer, wait=wait, timeout=timeout))

    def stories_get_peer_max_i_ds(self, *, id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_get_peer_max_i_ds(id=id, wait=wait, timeout=timeout))

    def stories_toggle_peer_stories_hidden(self, *, peer: Any, hidden: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.stories_toggle_peer_stories_hidden(peer=peer, hidden=hidden, wait=wait, timeout=timeout))

    def premium_get_boosts_list(self, *, peer: Any, offset: Any, limit: Any, gifts: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.premium_get_boosts_list(peer=peer, offset=offset, limit=limit, gifts=gifts, wait=wait, timeout=timeout))

    def premium_get_my_boosts(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.premium_get_my_boosts(wait=wait, timeout=timeout))

    def premium_apply_boost(self, *, peer: Any, slots: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.premium_apply_boost(peer=peer, slots=slots, wait=wait, timeout=timeout))

    def premium_get_boosts_status(self, *, peer: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.premium_get_boosts_status(peer=peer, wait=wait, timeout=timeout))

    def third_party_request(self, *, message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.third_party_request(message=message, wait=wait, timeout=timeout))

    def third_party_tell(self, *, message: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.third_party_tell(message=message, wait=wait, timeout=timeout))

    def help_get_timezones_list(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.help_get_timezones_list(hash=hash, wait=wait, timeout=timeout))

    def account_update_business_work_hours(self, *, business_work_hours: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_business_work_hours(business_work_hours=business_work_hours, wait=wait, timeout=timeout))

    def account_update_birthday(self, *, birthday: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_birthday(birthday=birthday, wait=wait, timeout=timeout))

    def contacts_get_birthdays(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.contacts_get_birthdays(wait=wait, timeout=timeout))

    def account_save_music(self, *, id: Any, unsave: Any=None, after_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_save_music(id=id, unsave=unsave, after_id=after_id, wait=wait, timeout=timeout))

    def account_set_main_profile_tab(self, *, tab: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_set_main_profile_tab(tab=tab, wait=wait, timeout=timeout))

    def account_get_saved_music_ids(self, *, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_get_saved_music_ids(hash=hash, wait=wait, timeout=timeout))

    def account_update_personal_channel(self, *, channel: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.account_update_personal_channel(channel=channel, wait=wait, timeout=timeout))

    def users_get_saved_music(self, *, id: Any, offset: Any, limit: Any, hash: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.users_get_saved_music(id=id, offset=offset, limit=limit, hash=hash, wait=wait, timeout=timeout))

    def users_get_saved_music_by_i_d(self, *, id: Any, documents: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.users_get_saved_music_by_i_d(id=id, documents=documents, wait=wait, timeout=timeout))

    def messages_toggle_dialog_filter_tags(self, *, enabled: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.messages_toggle_dialog_filter_tags(enabled=enabled, wait=wait, timeout=timeout))

    def req_pq(self, *, nonce: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.req_pq(nonce=nonce, wait=wait, timeout=timeout))

    def req_pq_multi(self, *, nonce: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.req_pq_multi(nonce=nonce, wait=wait, timeout=timeout))

    def req_pq_multi_new(self, *, nonce: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.req_pq_multi_new(nonce=nonce, wait=wait, timeout=timeout))

    def req__d_h_params(self, *, nonce: Any, server_nonce: Any, p: Any, q: Any, public_key_fingerprint: Any, encrypted_data: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.req__d_h_params(nonce=nonce, server_nonce=server_nonce, p=p, q=q, public_key_fingerprint=public_key_fingerprint, encrypted_data=encrypted_data, wait=wait, timeout=timeout))

    def set_client__d_h_params(self, *, nonce: Any, server_nonce: Any, encrypted_data: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.set_client__d_h_params(nonce=nonce, server_nonce=server_nonce, encrypted_data=encrypted_data, wait=wait, timeout=timeout))

    def destroy_auth_key(self, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.destroy_auth_key(wait=wait, timeout=timeout))

    def ping(self, *, ping_id: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.ping(ping_id=ping_id, wait=wait, timeout=timeout))

    def ping_delay_disconnect(self, *, ping_id: Any, disconnect_delay: Any, wait: Any=True, timeout: Any=30):
        return self._run(self._client.ping_delay_disconnect(ping_id=ping_id, disconnect_delay=disconnect_delay, wait=wait, timeout=timeout))

    def invoke(self, method: Any, *, wait: Any=True, timeout: Any=30, **payload):
        return self._run(self._client.invoke(method=method, wait=wait, timeout=timeout, **payload))

    def send(self, chat_id: Any, text: Any, *, reply_to_message_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.send(chat_id=chat_id, text=text, reply_to_message_id=reply_to_message_id, wait=wait, timeout=timeout))

    def send_message(self, chat_id: Any, text: Any, *, reply_to_message_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.send_message(chat_id=chat_id, text=text, reply_to_message_id=reply_to_message_id, wait=wait, timeout=timeout))

    def get_me(self):
        return self._run(self._client.get_me())

    def get_messages(self, chat_id: Any, *, limit: Any=20, ids: Any=None):
        return self._run(self._client.get_messages(chat_id=chat_id, limit=limit, ids=ids))

    def get_message(self, chat_id: Any, message_id: Any):
        return self._run(self._client.get_message(chat_id=chat_id, message_id=message_id))

    def get_chats(self, *, limit: Any=100):
        return self._run(self._client.get_chats(limit=limit))

    def download(self, message: Any, destination: Any=None):
        return self._run(self._client.download(message=message, destination=destination))

    def download_media(self, message: Any, destination: Any=None):
        return self._run(self._client.download_media(message=message, destination=destination))

    def forward_message(self, source_chat_id: Any, message_id: Any, destination_chat_id: Any, *, wait: Any=True, timeout: Any=30):
        return self._run(self._client.forward_message(source_chat_id=source_chat_id, message_id=message_id, destination_chat_id=destination_chat_id, wait=wait, timeout=timeout))

    def send_file(self, chat_id: Any, file: Any, *, caption: Any=None, reply_to_message_id: Any=None, mime_type: Any=None, attributes: Any=None, thumbnail: Any=None, wait: Any=True, timeout: Any=300):
        return self._run(self._client.send_file(chat_id=chat_id, file=file, caption=caption, reply_to_message_id=reply_to_message_id, mime_type=mime_type, attributes=attributes, thumbnail=thumbnail, wait=wait, timeout=timeout))

    def send_photo(self, chat_id: Any, photo: Any, *, caption: Any=None, reply_to_message_id: Any=None, wait: Any=True, timeout: Any=300):
        return self._run(self._client.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_to_message_id=reply_to_message_id, wait=wait, timeout=timeout))

    def send_video(self, chat_id: Any, video: Any, *, caption: Any=None, reply_to_message_id: Any=None, wait: Any=True, timeout: Any=300):
        return self._run(self._client.send_video(chat_id=chat_id, video=video, caption=caption, reply_to_message_id=reply_to_message_id, wait=wait, timeout=timeout))

    def send_voice(self, chat_id: Any, voice: Any, *, duration: Any, caption: Any=None, reply_to_message_id: Any=None, wait: Any=True, timeout: Any=300):
        return self._run(self._client.send_voice(chat_id=chat_id, voice=voice, duration=duration, caption=caption, reply_to_message_id=reply_to_message_id, wait=wait, timeout=timeout))

    def send_poll(self, chat_id: Any, question: Any, options: Any, *, anonymous: Any=True, multiple: Any=False, correct_option: Any=None, reply_to_message_id: Any=None, wait: Any=True, timeout: Any=30):
        return self._run(self._client.send_poll(chat_id=chat_id, question=question, options=options, anonymous=anonymous, multiple=multiple, correct_option=correct_option, reply_to_message_id=reply_to_message_id, wait=wait, timeout=timeout))

    def get_operation(self, operation_id: Any):
        return self._run(self._client.get_operation(operation_id=operation_id))

    def wait_operation(self, operation_id: Any, *, timeout: Any=30):
        return self._run(self._client.wait_operation(operation_id=operation_id, timeout=timeout))

    def run(self, *, workers: Any=1):
        return self._run(self._client.run(workers=workers))

    def export_session(self, destination: Any):
        return self._run(self._client.export_session(destination=destination))
