#Note: Appending $ will anchor the command
#provide both anchored and unachored commands via 'over'
phrase <user.text>$:
    user.add_phrase_to_history(text)
    insert(text)
phrase <user.text> over:
    user.add_phrase_to_history(text)
    insert(text)
{user.prose_formatter} <user.prose>$: user.insert_formatted(prose, prose_formatter)
{user.prose_formatter} <user.prose> over: user.insert_formatted(prose, prose_formatter)
<user.format_text>+$: user.insert_many(format_text_list)
<user.format_letters>+$: user.insert_many(format_letters_list)
<user.format_text>+ [over]: user.insert_many(format_text_list)
<user.formatters> that: user.formatters_reformat_selection(user.formatters)
(only | lonely) <user.word>: user.add_phrase_to_history(user.word)
format help: user.formatters_help_toggle()

recent list: user.toggle_phrase_history()
recent close: user.phrase_history_hide()
recent repeat <number_small>:
    recent_phrase = user.get_recent_phrase(number_small)
    user.add_phrase_to_history(recent_phrase)
    insert(recent_phrase)
recent copy <number_small>: clip.set_text(user.get_recent_phrase(number_small))
select that: user.select_last_phrase()
before that: user.before_last_phrase()
(nope that | scratch that): user.clear_last_phrase()
nope that was <user.formatters>: user.formatters_reformat_last(formatters)

# @rntz recommendation on slack
#<user.format_text>+ [over]: user.insert_many(format_text_list)
#(<user.formatters> exactly | phrase) <user.text>$:
#  user.insert_formatted(text, formatters or "NOOP")
