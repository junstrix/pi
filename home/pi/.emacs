;; (let ((buffer (url-retrieve-synchronously
;; 		        "http://tromey.com/elpa/package-install.el")))
;; (save-excursion
;;   (set-buffer buffer)
;;   (goto-char (point-min))
;;   (re-search-forward "^$" nil 'move)
;;   (eval-region (point) (point-max))
;;   (kill-buffer (current-buffer))))
;;; This was installed by package-install.el.
;;; This provides support for the package system and
;;; interfacing with ELPA, the package archive.
;;; Move this code earlier if you want to reference
;;; packages in your .emacs.
(when
    (load
     (expand-file-name "~/.emacs.d/elpa/package.el")) ;emacs23 use low version on github(see getpacket)
  (add-to-list 'package-archives
	     '("melpa" . "http://melpa.milkbox.net/packages/") t)
  (package-initialize))
