# Is this file is specifically for when the wiki is open
# XXX - detect the actual wiki rather than markdown
# See https://github.com/vimwiki/vimwiki/
tag: user.vim_wiki
and tag: user.markdown
-

###
# Internal Vim Wiki Commands
#
# Only accessible when operating inside of a wiki file
###

wiki link: user.vim_command_mode(":VimwikiFollowLink\n")
wiki back: user.vim_command_mode(":VimwikiGoBackLink\n")
wiki split link: user.vim_command_mode(":VimwikiVSplitLink\n")
wiki tab link: user.vim_command_mode(":VimwikiTabnewLink\n")
wiki next link: user.vim_command_mode(":VimwikiNextLink\n")

# Convenience for when you aren't directly on the link
go [next] link:
    user.vim_command_mode(":VimwikiNextLink\n")
    user.vim_command_mode(":VimwikiFollowLink\n")
wiki last link: user.vim_command_mode(":VimwikiPrevLink\n")
wiki go to: user.vim_command_mode(":VimwikiGoto ")
wiki rename: user.vim_command_mode(":VimwikiRenameFile ")
wiki next task: user.vim_command_mode(":VimwikiNextTask\n")
# XXX - todo HTML stuff
wiki toggle: user.vim_command_mode(":VimwikiToggleListItem\n")
wiki toggle reject: user.vim_command_mode(":VimwikiToggleRejectedListItem\n")

# XXX - right, left, etc
# wiki list right:
#     user.vim_command_mode(":VimwikiListChangeLevel >>\n")
# wiki list left:
#     user.vim_command_mode(":VimwikiListChangeLevel <<\n")

wiki search: user.vim_command_mode(":VimwikiSearch ")
wiki find links: user.vim_command_mode(":VimwikiBacklinks\n")

wiki table: user.vim_command_mode(":VimwikiTable\n")
wiki <number_small> by <number_small> table:
    user.vim_command_mode(":VimwikiTable {number_small_1} {number_small_2}\n")
wiki <number_small> table: user.vim_command_mode(":VimwikiTable {number_small}\n")
wiki move call left: user.vim_command_mode(":VimwikiTableMoveColumnLeft\n")
wiki move call right: user.vim_command_mode(":VimwikiTableMoveColumnRight\n")

# TODO - change command to update wiki?
wiki generate links: user.vim_command_mode(":VimwikiGenerateLinks")
# TODO - change command to update diary?
wiki generate diary links: user.vim_command_mode(":VimwikiDiaryGenerateLinks\n")
# :VimwikiDiaryNextDay - redundant? See global diary next
# :VimwikiDiaryPrevDay - redundant? See global diary last
wiki talk: user.vim_command_mode(":VimwikiTOC\n")
wiki check links: user.vim_command_mode(":VimwikiCheckLinks\n")
wiki rebuild tags: user.vim_command_mode(":VimwikiRebuildTags\n")
wiki search tags: user.vim_command_mode(":VimwikiSearchTags\n")
wiki generate tag links: user.vim_command_mode(":VimwikiGenerateTagLinks\n")

###
# VimWiki Syntax
#
# TODO - Start from 5. Wiki syntax in :help vimwiki
###
