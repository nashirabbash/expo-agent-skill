---
title: "SystemUI"
description: "A library that allows interacting with system UI elements."
source_url: "https://docs.expo.dev/versions/latest/sdk/system-ui.md"
scraped_at: "2026-07-15T08:43:54.727176"
---

---
title: SystemUI
description: A library that allows interacting with system UI elements.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-system-ui'
packageName: 'expo-system-ui'
platforms: ['android', 'ios', 'tvos', 'web']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Expo SystemUI

A library that allows interacting with system UI elements.
Android, iOS, tvOS, Web

`expo-system-ui` enables you to interact with UI elements that fall outside of the React tree. Specifically the root view background color, and locking the user interface style globally on Android.

## Installation

```sh
# npm
npx expo install expo-system-ui

# yarn
yarn expo install expo-system-ui

# pnpm
pnpm expo install expo-system-ui

# bun
bun expo install expo-system-ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Configuration in app config

You can configure `expo-system-ui` using its built-in [config plugin](/config-plugins/introduction.md) if you use config plugins in your project ([Continuous Native Generation (CNG)](/workflow/continuous-native-generation.md)). The plugin allows you to configure [`userInterfaceStyle`](/versions/latest/config/app.md#userinterfacestyle) on Android and [`backgroundColor`](/versions/latest/config/app.md#backgroundcolor) on iOS properties from [app config](/versions/latest/config/app.md). These properties cannot be set at runtime and require building a new app binary to take effect. If your app does **not** use CNG, then you'll need to manually configure the library.

### Example app.json with config plugin

```json
{
  "expo": {
    "backgroundColor": "#ffffff",
    "userInterfaceStyle": "light",
    "ios": {
      "backgroundColor": "#ffffff",
    }
    "android": {
      "userInterfaceStyle": "light"
    },
    "plugins": ["expo-system-ui"],
  }
}
```

#### Are you using this library in an existing React Native app?

If you're not using Continuous Native Generation ([CNG](/workflow/continuous-native-generation.md)) or you're using native **android** and **ios** project manually, then you need to add the following configuration to your native project:

**Android**

To apply `userInterfaceStyle` on Android, you need to add the `expo_system_ui_user_interface_style` configuration **android/app/src/main/res/values/strings.xml**:

```xml
<resources>
  <!-- ... -->
  <string name="expo_system_ui_user_interface_style" translatable="false">light</string> <!-- or dark -->
</resources>
```

**iOS**

To apply `backgroundColor` on iOS, you need to add the `UIUserInterfaceStyle` configuration in **ios/your-app/Info.plist**:

```xml
<plist>
  <dict>
    <!-- ... -->
    <key>UIUserInterfaceStyle</key>
    <string>Light</string> <!-- or Dark -->
  </dict>
</plist>
```

## API

```js
import * as SystemUI from 'expo-system-ui';
```

## Methods

### `SystemUI.getBackgroundColorAsync()`

Supported platforms: Android, iOS, tvOS, Web.

Gets the root view background color.

Returns: `Promise<colorvalue>`

Current root view background color in hex format. Returns `null` if the background color is not set.

Example

```ts
const color = await SystemUI.getBackgroundColorAsync();
```

### `SystemUI.setBackgroundColorAsync(color)`

Supported platforms: Android, iOS, tvOS, Web.

| Parameter | Type | Description |
| --- | --- | --- |
| `color` | [ColorValue](https://reactnative.dev/docs/colors) | null | Any valid [CSS 3 (SVG) color](http://www.w3.org/TR/css3-color/#svg-color). |

  

Changes the root view background color. Call this function in the root file outside of your component.

Returns: `Promise<void>`

Example

```ts
SystemUI.setBackgroundColorAsync("black");
```
