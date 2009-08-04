;; (defvar projdir/project-frames (make-hash-table) "The current list of projects which projdir can see"
(setq projdir/project-frames (make-hash-table :test 'equal))

(defun projdir/get-project (file)
  (apply 'concat (apply 'list (reverse (cdr (reverse (split-string (expand-file-name file) "/")))))))

(defun projdir/open-frame-by-project (projname)
  (let ((projframe (gethash projname projdir/project-frames nil)))
    (if projframe 
	(select-frame-by-name projname)
      (progn
	(puthash projname (make-frame (cons (cons 'name projname) nil)) projdir/project-frames)
	(select-frame-by-name projname)
	))))

(defun projdir-find-file (file)
  (interactive "f")
  (projdir/open-frame-by-project (projdir/get-project (expand-file-name file)))
  (find-file (expand-file-name file)))







