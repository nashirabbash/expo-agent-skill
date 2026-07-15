---
title: "DropdownMenu"
description: "A Jetpack Compose DropdownMenu component for displaying dropdown menus."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/dropdownmenu.md"
scraped_at: "2026-07-15T09:00:29.702521"
---

---
title: DropdownMenu
description: A Jetpack Compose DropdownMenu component for displaying dropdown menus.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# DropdownMenu

A Jetpack Compose DropdownMenu component for displaying dropdown menus.
Android, Included in Expo Go

Expo UI DropdownMenu matches the official Jetpack Compose [Menu API](https://developer.android.com/develop/ui/compose/components/menu) and displays a dropdown menu when a trigger element is pressed.

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

### Basic dropdown menu

```tsx
import {
  Host,
  DropdownMenu,
  DropdownMenuItem,
  OutlinedButton,
  Text,
  Icon,
} from '@expo/ui/jetpack-compose';
import { useState } from 'react';

const homeIcon = require('./assets/home.xml');

export default function BasicDropdownMenuExample() {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <Host matchContents>
      <DropdownMenu expanded={isExpanded} onDismissRequest={() => setIsExpanded(false)}>
        <DropdownMenu.Trigger>
          <OutlinedButton onClick={() => setIsExpanded(true)}>Show Menu</OutlinedButton>
        </DropdownMenu.Trigger>
        <DropdownMenu.Items>
          <DropdownMenuItem
            onClick={() => {
              setIsExpanded(false);
              console.log('Home pressed');
            }}>
            <DropdownMenuItem.Text>
              <Text>Home</Text>
            </DropdownMenuItem.Text>
            <DropdownMenuItem.LeadingIcon>
              <Icon source={homeIcon} size={24} />
            </DropdownMenuItem.LeadingIcon>
          </DropdownMenuItem>
        </DropdownMenu.Items>
      </DropdownMenu>
    </Host>
  );
}
```

### React Native components as trigger

You can use a React Native view (such as `Pressable`) as the dropdown's trigger by wrapping it in [`RNHostView`](/versions/latest/sdk/ui/jetpack-compose/rnhostview.md).

```tsx
import {
  Host,
  DropdownMenu,
  DropdownMenuItem,
  Text as ComposeText,
  RNHostView,
} from '@expo/ui/jetpack-compose';
import { useState } from 'react';
import { Pressable, Text } from 'react-native';

export default function RNTriggerDropdownMenuExample() {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <Host matchContents>
      <DropdownMenu expanded={isExpanded} onDismissRequest={() => setIsExpanded(false)}>
        <DropdownMenu.Trigger>
          <RNHostView matchContents>
            <Pressable
              onPress={() => setIsExpanded(true)}
              style={{
                alignSelf: 'flex-start',
                paddingHorizontal: 16,
                paddingVertical: 10,
                borderRadius: 8,
                backgroundColor: '#9B59B6',
              }}>
              <Text style={{ color: 'white', fontWeight: '600' }}>RN Pressable Trigger</Text>
            </Pressable>
          </RNHostView>
        </DropdownMenu.Trigger>
        <DropdownMenu.Items>
          <DropdownMenuItem onClick={() => setIsExpanded(false)}>
            <DropdownMenuItem.Text>
              <ComposeText>Item 1</ComposeText>
            </DropdownMenuItem.Text>
          </DropdownMenuItem>
          <DropdownMenuItem onClick={() => setIsExpanded(false)}>
            <DropdownMenuItem.Text>
              <ComposeText>Item 2</ComposeText>
            </DropdownMenuItem.Text>
          </DropdownMenuItem>
        </DropdownMenu.Items>
      </DropdownMenu>
    </Host>
  );
}
```

### Long-press trigger

Jetpack Compose has no dedicated long-press menu primitive — you compose one from a [`combinedClickable`](/versions/latest/sdk/ui/jetpack-compose/modifiers.md) modifier on the trigger view plus the existing controlled `DropdownMenu`. The menu anchors to the trigger automatically.

```tsx
import { Host, DropdownMenu, DropdownMenuItem, Text } from '@expo/ui/jetpack-compose';
import { background, combinedClickable } from '@expo/ui/jetpack-compose/modifiers';
import { useState } from 'react';

export default function LongPressDropdownMenuExample() {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <Host matchContents>
      <DropdownMenu expanded={isExpanded} onDismissRequest={() => setIsExpanded(false)}>
        <DropdownMenu.Trigger>
          <Text
            modifiers={[
              background('#e0e0e0'),
              combinedClickable({
                onClick: () => console.log('Short tap'),
                onLongClick: () => setIsExpanded(true),
              }),
            ]}>
            Long-press me
          </Text>
        </DropdownMenu.Trigger>
        <DropdownMenu.Items>
          <DropdownMenuItem onClick={() => setIsExpanded(false)}>
            <DropdownMenuItem.Text>
              <Text>Copy</Text>
            </DropdownMenuItem.Text>
          </DropdownMenuItem>
          <DropdownMenuItem
            elementColors={{ textColor: '#B3261E' }}
            onClick={() => setIsExpanded(false)}>
            <DropdownMenuItem.Text>
              <Text>Delete</Text>
            </DropdownMenuItem.Text>
          </DropdownMenuItem>
        </DropdownMenu.Items>
      </DropdownMenu>
    </Host>
  );
}
```

## API

```tsx
import { DropdownMenu } from '@expo/ui/jetpack-compose';
```

## Components

### `DropdownMenu`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DropdownMenuProps](#dropdownmenuprops)\>

Props of the `DropdownMenu` component.

DropdownMenuProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The contents of the submenu are used as an anchor for the dropdown menu. The children will be wrapped in a pressable element, which triggers opening of the dropdown menu.

### `color`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The color of the container holding the dropdown menu items.

### `expanded`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the dropdown menu is expanded (visible).

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onDismissRequest`

Supported platforms: Android.

Optional • Type: `() => void`

Callback fired when the menu requests to be dismissed (e.g. tapping outside). Must be provided when `expanded` is `true` to allow the menu to close.

### `style`

Supported platforms: Android.

Optional • Type: StyleProp<[ViewStyle](https://reactnative.dev/docs/view-style-props)\>

Optional styles to apply to the `DropdownMenu`.

### `DropdownMenuItem`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DropdownMenuItemProps](#dropdownmenuitemprops)\>

A dropdown menu item component that wraps Compose's `DropdownMenuItem`. Should be used inside `DropdownMenu.Items` or `ExposedDropdownMenu`.

### `Items`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<{ children: [ReactNode](https://reactnative.dev/docs/react-node) }\>

Container for items displayed in the dropdown menu. Children should be `DropdownMenuItem` components or other native views.

### `Preview`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<{ children: [ReactNode](https://reactnative.dev/docs/react-node) }\>

Preview content shown during long press (iOS only).

### `Trigger`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<{ children: [ReactNode](https://reactnative.dev/docs/react-node) }\>

Container for the trigger element that opens the dropdown menu.
