---
title: "NavigationBar"
description: "A Jetpack Compose NavigationBar component for Material 3 bottom navigation."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/navigationbar.md"
scraped_at: "2026-07-15T09:00:51.818235"
---

---
title: NavigationBar
description: A Jetpack Compose NavigationBar component for Material 3 bottom navigation.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# NavigationBar

A Jetpack Compose NavigationBar component for Material 3 bottom navigation.
Android, Included in Expo Go

Expo UI NavigationBar matches the official Jetpack Compose [`NavigationBar`](https://developer.android.com/develop/ui/compose/components/navigation-bar) API. It displays a row of destinations for switching between top-level app sections.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic navigation bar

Manage the selected item in React state and pass `selected` to each `NavigationBarItem`.

```tsx
import { useState } from 'react';
import { Host, Icon, NavigationBar, NavigationBarItem, Text } from '@expo/ui/jetpack-compose';

const HOME_ICON = require('./assets/home.xml');
const SEARCH_ICON = require('./assets/search.xml');
const SETTINGS_ICON = require('./assets/settings.xml');

export default function BasicNavigationBar() {
  const [selectedTab, setSelectedTab] = useState('home');

  return (
    <Host matchContents>
      <NavigationBar>
        <NavigationBarItem selected={selectedTab === 'home'} onClick={() => setSelectedTab('home')}>
          <NavigationBarItem.Icon>
            <Icon source={HOME_ICON} />
          </NavigationBarItem.Icon>
          <NavigationBarItem.Label>
            <Text>Home</Text>
          </NavigationBarItem.Label>
        </NavigationBarItem>

        <NavigationBarItem
          selected={selectedTab === 'search'}
          onClick={() => setSelectedTab('search')}>
          <NavigationBarItem.Icon>
            <Icon source={SEARCH_ICON} />
          </NavigationBarItem.Icon>
          <NavigationBarItem.Label>
            <Text>Search</Text>
          </NavigationBarItem.Label>
        </NavigationBarItem>

        <NavigationBarItem
          selected={selectedTab === 'settings'}
          onClick={() => setSelectedTab('settings')}>
          <NavigationBarItem.Icon>
            <Icon source={SETTINGS_ICON} />
          </NavigationBarItem.Icon>
          <NavigationBarItem.Label>
            <Text>Settings</Text>
          </NavigationBarItem.Label>
        </NavigationBarItem>
      </NavigationBar>
    </Host>
  );
}
```

## API

```tsx
import { NavigationBar, NavigationBarItem } from '@expo/ui/jetpack-compose';
```

## Components

### `NavigationBar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[NavigationBarProps](#navigationbarprops)\>

A Material Design 3 navigation bar.

NavigationBarProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Navigation bar items.

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors) • Default: `NavigationBarDefaults.containerColor`

Background color of the navigation bar.

### `contentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors) • Default: `contentColorFor(containerColor)`

Preferred content color inside the navigation bar.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `tonalElevation`

Supported platforms: Android.

Optional • Type: `number` • Default: `NavigationBarDefaults.Elevation`

Tonal elevation in dp.

### `NavigationBarItem`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[NavigationBarItemProps](#navigationbaritemprops)\>

A Material Design 3 navigation bar item. Must be used inside `NavigationBar`.

NavigationBarItemProps

### `alwaysShowLabel`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether to always show the label.

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing `Icon`, `SelectedIcon`, and `Label` slots.

### `colors`

Supported platforms: Android.

Optional • Type: [NavigationBarItemColors](#navigationbaritemcolors)

Colors for the item in different states.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the item is enabled.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the item is clicked.

### `selected`

Supported platforms: Android.

Type: `boolean`

Whether this item is currently selected.

## Types

### `NavigationBarItemColors`

Supported platforms: Android.

Colors for navigation bar items in different states.

| Property | Type | Description |
| --- | --- | --- |
| disabledIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedIndicatorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unselectedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unselectedTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

## Components

### `NavigationBar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[NavigationBarProps](#navigationbarprops)\>

A Material Design 3 navigation bar.

NavigationBarProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Navigation bar items.

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors) • Default: `NavigationBarDefaults.containerColor`

Background color of the navigation bar.

### `contentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors) • Default: `contentColorFor(containerColor)`

Preferred content color inside the navigation bar.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `tonalElevation`

Supported platforms: Android.

Optional • Type: `number` • Default: `NavigationBarDefaults.Elevation`

Tonal elevation in dp.

### `NavigationBarItem`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[NavigationBarItemProps](#navigationbaritemprops)\>

A Material Design 3 navigation bar item. Must be used inside `NavigationBar`.

NavigationBarItemProps

### `alwaysShowLabel`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether to always show the label.

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing `Icon`, `SelectedIcon`, and `Label` slots.

### `colors`

Supported platforms: Android.

Optional • Type: [NavigationBarItemColors](#navigationbaritemcolors)

Colors for the item in different states.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the item is enabled.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the item is clicked.

### `selected`

Supported platforms: Android.

Type: `boolean`

Whether this item is currently selected.

## Types

### `NavigationBarItemColors`

Supported platforms: Android.

Colors for navigation bar items in different states.

| Property | Type | Description |
| --- | --- | --- |
| disabledIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedIndicatorColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| selectedTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unselectedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| unselectedTextColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
