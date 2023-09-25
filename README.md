# ebook-paragraph-fixer-app

This is an app that fixes incorrectly formatted paragraphs in ebooks. It is especially useful for ebooks from the Gutenberg Project.

The ebooks in epub format from the Gutenberg project have a small bug that causes the text-to-speech engine not to work properly. It's because of the HTML files in the ebooks.

Every paragraph of a book is written in between paragraph tags, but there are many unintended new lines in them. This causes the TTS engine to read the ebook with unintended pauses, which ruins the experience when one wants to listen to the book rather than just read it.

So this app can fix those paragraphs and, ultimately, the HTML files.

In the current stage, it requires some manual work.

1) By using special ebook reader and editor apps, open an ebook to edit. (I advise Calibre.)

2) Copy the contents of an HTML page to the app, get the fixed page, and replace it with the original page.

3) Repeat the process with other pages and save the changes.

That's it!

P.S. I'm intending to make the app do the task automatically with minimal manual interference in the future.

