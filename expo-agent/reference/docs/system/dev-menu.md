---
title: "DevMenu"
description: "A library that provides a developer menu for debug builds."
source_url: "https://docs.expo.dev/versions/latest/sdk/dev-menu.md"
scraped_at: "2026-07-15T08:43:25.431110"
---

---
title: DevMenu
description: A library that provides a developer menu for debug builds.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-dev-menu'
packageName: 'expo-dev-menu'
platforms: ['android', 'ios', 'tvos']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Expo DevMenu

A library that provides a developer menu for debug builds.
Android, iOS, tvOS

The `expo-dev-menu` can be used as a **standalone library** in any Expo project. It is especially useful in [brownfield apps](/versions/latest/sdk/brownfield.md) that don't need the full [`expo-dev-client`](/versions/latest/sdk/dev-client.md) launcher interface.

`expo-dev-menu` provides a developer menu UI for React Native apps that includes:

-   A powerful and extensible menu UI accessible via shake gesture or three-finger long press
-   Quick access to common development actions
-   Support for custom menu items to extend functionality

## Installation

```sh
# npm
npx expo install expo-dev-menu

# yarn
yarn expo install expo-dev-menu

# pnpm
pnpm expo install expo-dev-menu

# bun
bun expo install expo-dev-menu
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

Once installed, the developer menu is available in your debug builds. You can open it by:

-   **Shake gesture**: Shake your device
-   **Three-finger long press**: Long press with three fingers on the screen
-   **Programmatically**: Call `DevMenu.openMenu()` from your code

## Extending the dev menu

The dev menu can be extended to include extra buttons by using the `registerDevMenuItems` API:

```tsx
import { registerDevMenuItems } from 'expo-dev-menu';

const devMenuItems = [
  {
    name: 'My Custom Button',
    callback: () => console.log('Hello world!'),
  },
];

registerDevMenuItems(devMenuItems);
```

This will create a new section in the dev menu that includes the buttons you have registered:

> **Note:** Subsequent calls of `registerDevMenuItems` will override all previous entries.

## Using with expo-dev-client

If you are using [development builds](/develop/development-builds/introduction.md), install `expo-dev-client` instead. It includes `expo-dev-menu` along with additional development tools:

-   A configurable launcher UI for switching between development servers
-   Improved debugging tools
-   Support for loading updates from [EAS Update](/eas-update/introduction.md)

```sh
npx expo install expo-dev-client
```

For more information, check the [`expo-dev-client` reference](/versions/latest/sdk/dev-client.md).

## API

```js
import * as DevMenu from 'expo-dev-menu';
```

## Methods

### `DevMenu.closeMenu()`

Supported platforms: Android, iOS, tvOS.

A method that closes development client menu when called.

Returns: `void`

### `DevMenu.hideMenu()`

Supported platforms: Android, iOS, tvOS.

A method that hides development client menu when called.

Returns: `void`

### `DevMenu.openMenu()`

Supported platforms: Android, iOS, tvOS.

A method that opens development client menu when called.

Returns: `void`

### `DevMenu.registerDevMenuItems(items)`

Supported platforms: Android, iOS, tvOS.

| Parameter | Type |
| --- | --- |
| `items` | [ExpoDevMenuItem[]](#expodevmenuitem) |

  

A method that allows to specify custom entries in the development client menu.

Returns: `Promise<void>`

## Types

### `ExpoDevMenuItem`

Supported platforms: Android, iOS, tvOS.

An object representing the custom development client menu entry.

| Property | Type | Description |
| --- | --- | --- |
| callback | `() => void` | Callback to fire, when user selects an item. |
| name | `string` | Name of the entry, will be used as label. |
| shouldCollapse(optional) | `boolean` | A boolean specifying if the menu should close after the user interaction. Default: `false` |
