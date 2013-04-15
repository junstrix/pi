syntax on
set guioptions=i
set number
set wildmenu
set incsearch
" set guifont=Source\ Code\ Pro\ 12
"ctags -R -f ~/.vim/systags /usr/include /usr/local/include
set tags+=~/.vim/systags
" ctags -R --sort=yes --c-kinds=+p --fields=+iaS --extra=+q --language-force=C++ -f glibc_tags ./glibc-2.17/
" set tags+=~/.vim/glibc_tags
" omnicomplete
" autocmd CursorMovedI * if pumvisible() == 0|pclose|endif
" autocmd InsertLeave * if pumvisible() == 0|pclose|endif
" set guifontwide=文泉驿等宽微米黑\ 12
let Tlist_Show_One_File = 1
let Tlist_Use_Right_Window = 1
let Tlist_Exit_OnlyWindow = 1
" let Tlist_Process_File_Always = 1
let Tlist_Show_Menu = 1
let ropevim_vim_completion=1
let ropevim_extended_complete=1
let g:statline_fugitive = 1
runtime ftplugin/man.vim
autocmd FileType vim set cursorline
autocmd FileType c set cursorline
autocmd FileType python set textwidth=79 tabstop=8 softtabstop=4 shiftwidth=4
autocmd FileType python set expandtab autoindent cursorline
autocmd FileType python set omnifunc=pythoncomplete
" autocmd FileType python set ft=python.django " For SnipMate
" autocmd FileType html set ft=htmldjango.html " For SnipMate
autocmd BufRead *.py set makeprg=python\ %
nmap <leader>py :w<CR>:make<CR>
" colorscheme torte
let mapleader = ";"
" normal-mode
nmap <leader>ws :w !sudo tee %<cr>
nmap <leader>n :bn<cr>
nmap <leader>e :e 
nmap <leader>co :colorscheme
" cd command-t && rake make
nmap <leader>ct :CommandT<CR>
nmap <leader>qa :qa<cr>
nmap <leader>w :w<cr>
nmap <leader>b :MiniBufExplorer<cr>
nmap <leader>s :source ~/.vimrc<cr>
nmap <leader>fl :NERDTreeToggle<cr>
nmap <leader>tl :TlistToggle<cr>
" DrawIt[!] start/stop DrawIt"
nmap <leader>dr :DrawIt
nmap <leader>re :registers<cr>
nmap <leader>r :w<CR>:make<CR>:cw<CR><CR>:!./a.out<CR>
" help cscope
" ctags -R
" cscope -Rb
" cscope add ...
nmap <C-s>s :cs find s <C-R>=expand("<cword>")<CR><CR>
nmap <C-s>g :cs find g <C-R>=expand("<cword>")<CR><CR>
nmap <C-s>c :cs find c <C-R>=expand("<cword>")<CR><CR>
nmap <C-s>t :cs find t <C-R>=expand("<cword>")<CR><CR>
nmap <C-s>e :cs find e <C-R>=expand("<cword>")<CR><CR>
nmap <C-s>f :cs find f <C-R>=expand("<cfile>")<CR><CR>
nmap <C-s>i :cs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
nmap <C-s>d :cs find d <C-R>=expand("<cword>")<CR><CR>
" nmap <leader>ct :!ctags -R --sort=yes --c++-kinds=+p --fields=+iaS --extra=+q .<CR>
" insert-mode
imap jk <Esc>
imap <C-b> <Left>
imap <C-f> <Right>
imap <C-a> <C-o>I
imap <C-e> <End>
imap <C-d> <Del>
imap <C-k> <C-o>D
" command-mode
" start of line
:cnoremap <C-A>		<Home>
" back one character
:cnoremap <C-B>		<Left>
" delete character under cursor
:cnoremap <C-D>		<Del>
" end of line
:cnoremap <C-E>		<End>
" forward one character
:cnoremap <C-F>		<Right>
" recall newer command-line
:cnoremap <C-N>		<Down>
" recall previous (older) command-line
:cnoremap <C-P>		<Up>
" back one word
:cnoremap <Esc><C-B>	<S-Left>
" forward one word
:cnoremap <Esc><C-F>	<S-Right>
"""""""""""""""""""""""""""""Configure for vundle"""""""""""""""""""""""""""""
set nocompatible               " be iMproved
filetype off                   " required!
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
" let Vundle manage Vundle
" required! 
Bundle 'gmarik/vundle'
" My Bundles here:
"
" original repos on github
Bundle 'tpope/vim-fugitive'
"Bundle 'Lokaltog/vim-easymotion'
"Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}
"Bundle 'tpope/vim-rails.git'
" vim-scripts repos
"Bundle 'L9'
"Bundle 'FuzzyFinder'
" non github repos
" Bundle 'git://git.wincent.com/command-t.git'
" ...
filetype plugin indent on     " required!
"
" Brief help
" :BundleList          - list configured bundles
" :BundleInstall(!)    - install(update) bundles
" :BundleSearch(!) foo - search(or refresh cache first) for foo
" :BundleClean(!)      - confirm(or auto-approve) removal of unused bundles
"
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Bundle command are not allowed..
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Bundle 'FencView.vim'
Bundle 'minibufexplorerpp'
Bundle 'msanders/snipmate.vim'
"Bundle 'DrawIt'
"" Bundle 'git://github.com/honza/snipmate-snippets.git'
"Bundle 'git://github.com/vim-scripts/matrix.vim--Yang.git'
Bundle 'git://github.com/vim-scripts/taglist.vim.git'
Bundle 'git://github.com/scrooloose/nerdtree.git'
Bundle 'Syntastic'
"" <leader>cc
Bundle 'git://github.com/scrooloose/nerdcommenter.git'
Bundle 'git://github.com/powerman/vim-plugin-viewdoc.git'
" Bundle 'git://github.com/vim-scripts/simple-pairs.git'
"Bundle 'git://github.com/sontek/rope-vim.git'
"Bundle 'git://github.com/scrooloose/vim-statline.git'
"Bundle 'git://github.com/flazz/vim-colorschemes.git'
"Bundle 'git://github.com/davidhalter/jedi-vim.git'
" Bundle 'git://github.com/vim-scripts/VimPdb.git'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" vim --versoin (+python +ruby)
" exuberant-ctags cscope
" pip install jedi
" colorscheme
" black       - molokai/tango/desert/ir_black/rootwater/made_of_code/blackbord
"		freya/koehler/django/darkblue
" other color - solarized/python
