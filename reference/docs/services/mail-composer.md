---
title: "MailComposer"
description: "A library that provides functionality to compose and send emails with the system's specific UI."
source_url: "https://docs.expo.dev/versions/latest/sdk/mail-composer.md"
scraped_at: "2026-07-15T08:41:56.227406"
---

---
title: MailComposer
description: A library that provides functionality to compose and send emails with the system's specific UI.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-mail-composer'
packageName: 'expo-mail-composer'
iconUrl: '/static/images/packages/expo-mail-composer.png'
platforms: ['android', 'ios*', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Expo MailComposer

A library that provides functionality to compose and send emails with the system's specific UI.
Android, iOS (device only), Web, Included in Expo Go

`expo-mail-composer` allows you to compose and send emails quickly and easily using the OS UI. This module can't be used on iOS Simulators since you can't sign into a mail account on them.

## Installation

```sh
# npm
npx expo install expo-mail-composer

# yarn
yarn expo install expo-mail-composer

# pnpm
pnpm expo install expo-mail-composer

# bun
bun expo install expo-mail-composer
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## API

```js
import * as MailComposer from 'expo-mail-composer';
```

## Methods

### `MailComposer.composeAsync(options)`

Supported platforms: Android, iOS, Web.

| Parameter | Type |
| --- | --- |
| `options` | [MailComposerOptions](#mailcomposeroptions) |

  

Opens a mail modal for iOS and a mail app intent for Android and fills the fields with provided data. On iOS you will need to be signed into the Mail app.

Returns: `Promise<mailcomposerresult>`

A promise fulfilled with an object containing a `status` field that specifies whether an email was sent, saved, or cancelled. Android does not provide this info, so the status is always set as if the email were sent.

### `MailComposer.getClients()`

Supported platforms: Android, iOS, Web.

Retrieves a list of available email clients installed on the device. This can be used to present options to the user for sending emails through their preferred email client, or to open an email client so the user can access their mailbox — for example, to open a confirmation email sent by your app.

Returns: `MailClient[]`

An array of available mail clients.

### `MailComposer.isAvailableAsync()`

Supported platforms: Android, iOS, Web.

Determine if the `MailComposer` API can be used in this app.

Returns: `Promise<boolean>`

A promise resolves to `true` if the API can be used, and `false` otherwise.

-   Returns `true` when the device has a default email setup for sending mail.
-   Can return `false` on iOS if an MDM profile is setup to block outgoing mail. If this is the case, you may want to use the Linking API instead.
-   Always returns `true` in the browser.

## Types

### `MailClient`

Supported platforms: Android, iOS, Web.

Represents a mail client available on the device.

| Property | Type | Description |
| --- | --- | --- |
| label | `string` | The display name of the mail client. |
| packageName(optional) | `string` | Supported platforms: Android. The package name of the mail client application. You can use this package name with the [`getApplicationIconAsync`](/versions/latest/sdk/intent-launcher.md#intentlaunchergetapplicationiconasyncpackagename) or [`openApplication`](/versions/latest/sdk/intent-launcher.md#intentlauncheropenapplicationpackagename) functions from [`expo-intent-launcher`](/versions/latest/sdk/intent-launcher.md) to retrieve the app’s icon or open the mail client directly. |
| url(optional) | `string` | Supported platforms: iOS. The URL scheme of the mail client. You can use this URL with the [`openURL`](/versions/latest/sdk/linking.md#linkingopenurlurl) function from [`expo-linking`](/versions/latest/sdk/linking.md) to open the mail client. |

### `MailComposerOptions`

Supported platforms: Android, iOS, Web.

A map defining the data to fill the mail.

| Property | Type | Description |
| --- | --- | --- |
| attachments(optional) | `string[]` | An array of app's internal file URIs to attach. |
| bccRecipients(optional) | `string[]` | An array of e-mail addresses of the BCC recipients. |
| body(optional) | `string` | Body of the e-mail. |
| ccRecipients(optional) | `string[]` | An array of e-mail addresses of the CC recipients. |
| isHtml(optional) | `boolean` | Whether the body contains HTML tags so it could be formatted properly. Not working perfectly on Android. |
| recipients(optional) | `string[]` | An array of e-mail addresses of the recipients. |
| subject(optional) | `string` | Subject of the e-mail. |

### `MailComposerResult`

Supported platforms: Android, iOS, Web.

| Property | Type | Description |
| --- | --- | --- |
| status | [MailComposerStatus](#mailcomposerstatus) | - |

## Enums

### `MailComposerStatus`

Supported platforms: Android, iOS, Web.

#### `CANCELLED`

`MailComposerStatus.CANCELLED = "cancelled"`

#### `SAVED`

`MailComposerStatus.SAVED = "saved"`

#### `SENT`

`MailComposerStatus.SENT = "sent"`

#### `UNDETERMINED`

`MailComposerStatus.UNDETERMINED = "undetermined"`
