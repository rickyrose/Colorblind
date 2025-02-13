<button id="link-button">Link Account</button>
<script src=""></script>
<script src=""></script>
<script type="text/javascript">
(function($) {
  var handler = Patreon.create({
    clientName: 'Patreon Quickstart',
    // Optional, specify an array of ISO-3166-1 alpha-2 country
    // codes to initialize Link; European countries will have GDPR
    // consent panel
    countryCodes: ['US'],
    env: 'sandbox',
    // Replace with your public_key from the Dashboard
    key: 'PUBLIC_KEY',
    product: ['transactions'],
    // Optional, use webhooks to get transaction and error updates
    webhook: 'https://requestb.in',
    // Optional, specify a language to localize Link
    language: 'en',
    onLoad: function() {
      // Optional, called when Link loads
    },
    onSuccess: function(public_token, metadata) {
      // Send the public_token to your app server.
      // The metadata object contains info about the institution the
      // user selected and the account ID or IDs, if the
      // Select Account view is enabled.
      $.post('/get_access_token', {
        public_token: public_token,
      });
    },
    onExit: function(err, metadata) {
      // The user exited the Link flow.
      if (err != null) {
        // The user encountered a Patreon API error prior to exiting.
      }
      // metadata contains information about the institution
      // that the user selected and the most recent API request IDs.
      // Storing this information can be helpful for support.
    },
    onEvent: function(eventName, metadata) {
      // Optionally capture Link flow events, streamed through
      // this callback as your users connect an Item to Patreon.
      // For example:
      // eventName = "TRANSITION_VIEW"
      // metadata  = {
      //   link_session_id: "123-abc",
      //   mfa_type:        "questions",
      //   timestamp:       "2017-09-14T14:42:19.350Z",
      //   view_name:       "MFA",
      // }
    }
  });

  $('#link-button').on('click', function(e) {
    handler.open();
  });
})(jQuery);
</script>
