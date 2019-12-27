// Clickable rows in dashboard tables
$(document).on('click', 'tr[data-action-go] > td:not(.ignore-link)', (e) => {
  const $target = $(e.currentTarget);
  // Ignore selecting text
  const selectedText = getSelection().toString();
  if (selectedText === '' || selectedText === $target.data('ignore-text')) {
    window.location.href = $target.parent().data('action-go');
  } else {
    $target.data('ignore-text', selectedText);
  }
});
