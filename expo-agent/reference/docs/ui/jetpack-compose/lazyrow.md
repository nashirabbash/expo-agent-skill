---
title: "LazyRow"
description: "A Jetpack Compose LazyRow component for displaying horizontally scrolling lists."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/lazyrow.md"
scraped_at: "2026-07-15T09:01:00.751323"
---

---
title: LazyRow
description: A Jetpack Compose LazyRow component for displaying horizontally scrolling lists.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# LazyRow

A Jetpack Compose LazyRow component for displaying horizontally scrolling lists.
Android, Included in Expo Go

A lazily-loaded horizontal list component that only renders visible items for efficient scrolling. See the [official Jetpack Compose documentation](https://developer.android.com/develop/ui/compose/lists) for more information.

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

### Basic lazy row

```tsx
import { Host, LazyRow, Text } from '@expo/ui/jetpack-compose';

const items = Array.from({ length: 100 }, (_, i) => `Item ${i + 1}`);

export default function BasicLazyRow() {
  return (
    <Host style={{ height: 100 }}>
      <LazyRow>
        {items.map(item => (
          <Text key={item}>{item}</Text>
        ))}
      </LazyRow>
    </Host>
  );
}
```

### With arrangement

Use the `horizontalArrangement` prop to control how items are spaced within the list. Pass a string value like `'spaceBetween'` or an object like `{ spacedBy: 8 }` for fixed spacing in dp.

```tsx
import { Host, LazyRow, Text } from '@expo/ui/jetpack-compose';

export default function LazyRowArrangement() {
  return (
    <Host style={{ height: 100 }}>
      <LazyRow horizontalArrangement={{ spacedBy: 16 }} verticalAlignment="center">
        <Text>Spaced item 1</Text>
        <Text>Spaced item 2</Text>
        <Text>Spaced item 3</Text>
      </LazyRow>
    </Host>
  );
}
```

### With content padding

Use the `contentPadding` prop to add padding around the list content in dp.

```tsx
import { Host, LazyRow, Text } from '@expo/ui/jetpack-compose';

export default function LazyRowPadding() {
  return (
    <Host style={{ height: 100 }}>
      <LazyRow contentPadding={{ start: 16, top: 8, end: 16, bottom: 8 }}>
        <Text>Padded item 1</Text>
        <Text>Padded item 2</Text>
        <Text>Padded item 3</Text>
      </LazyRow>
    </Host>
  );
}
```

## API

```tsx
import { LazyRow } from '@expo/ui/jetpack-compose';
```

## Component

### `LazyRow`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LazyRowProps](#lazyrowprops)\>

A lazy row component that efficiently displays a horizontally scrolling list.

LazyRowProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the lazy row.

### `contentPadding`

Supported platforms: Android.

Optional • Type: [ContentPadding](#contentpadding)

Content padding in dp.

### `horizontalArrangement`

Supported platforms: Android.

Optional • Literal type: `union`

The horizontal arrangement of items. Can be a preset string or an object with `spacedBy` to specify spacing in dp.

Acceptable values are: `'start'` | `'end'` | `'center'` | `'spaceBetween'` | `'spaceAround'` | `'spaceEvenly'` | `{ spacedBy: number }`

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `verticalAlignment`

Supported platforms: Android.

Optional • Literal type: `string`

The vertical alignment of items.

Acceptable values are: `'center'` | `'top'` | `'bottom'`
