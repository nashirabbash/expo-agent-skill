---
title: "LazyColumn"
description: "A Jetpack Compose LazyColumn component for displaying scrollable lists."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/lazycolumn.md"
scraped_at: "2026-07-15T09:00:34.648650"
---

---
title: LazyColumn
description: A Jetpack Compose LazyColumn component for displaying scrollable lists.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# LazyColumn

A Jetpack Compose LazyColumn component for displaying scrollable lists.
Android, Included in Expo Go

A lazily-loaded vertical list component that only renders visible items for efficient scrolling. See the [official Jetpack Compose documentation](https://developer.android.com/develop/ui/compose/lists) for more information.

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

### Basic lazy column

```tsx
import { Host, LazyColumn, ListItem, Text } from '@expo/ui/jetpack-compose';

const items = Array.from({ length: 100 }, (_, i) => `Item ${i + 1}`);

export default function BasicLazyColumn() {
  return (
    <Host style={{ height: 400 }}>
      <LazyColumn>
        {items.map(item => (
          <ListItem key={item}>
            <ListItem.HeadlineContent>
              <Text>{item}</Text>
            </ListItem.HeadlineContent>
          </ListItem>
        ))}
      </LazyColumn>
    </Host>
  );
}
```

### With arrangement

Use the `verticalArrangement` prop to control how items are spaced within the list. Pass a string value like `'spaceBetween'` or an object like `{ spacedBy: 8 }` for fixed spacing in dp.

```tsx
import { Host, LazyColumn, ListItem, Text } from '@expo/ui/jetpack-compose';

export default function LazyColumnArrangement() {
  return (
    <Host style={{ height: 400 }}>
      <LazyColumn verticalArrangement={{ spacedBy: 8 }} horizontalAlignment="center">
        <ListItem>
          <ListItem.HeadlineContent>
            <Text>Spaced Item 1</Text>
          </ListItem.HeadlineContent>
        </ListItem>
        <ListItem>
          <ListItem.HeadlineContent>
            <Text>Spaced Item 2</Text>
          </ListItem.HeadlineContent>
        </ListItem>
        <ListItem>
          <ListItem.HeadlineContent>
            <Text>Spaced Item 3</Text>
          </ListItem.HeadlineContent>
        </ListItem>
      </LazyColumn>
    </Host>
  );
}
```

### With content padding

Use the `contentPadding` prop to add padding around the list content in dp.

```tsx
import { Host, LazyColumn, ListItem } from '@expo/ui/jetpack-compose';

export default function LazyColumnPadding() {
  return (
    <Host style={{ height: 400 }}>
      <LazyColumn contentPadding={{ start: 16, top: 8, end: 16, bottom: 8 }}>
        <ListItem>
          <ListItem.HeadlineContent>Padded item 1</ListItem.HeadlineContent>
        </ListItem>
        <ListItem>
          <ListItem.HeadlineContent>Padded item 2</ListItem.HeadlineContent>
        </ListItem>
        <ListItem>
          <ListItem.HeadlineContent>Padded item 3</ListItem.HeadlineContent>
        </ListItem>
      </LazyColumn>
    </Host>
  );
}
```

## API

```tsx
import { LazyColumn } from '@expo/ui/jetpack-compose';
```

## Component

### `LazyColumn`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LazyColumnProps](#lazycolumnprops)\>

A lazy column component that efficiently displays a vertically scrolling list.

LazyColumnProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to display inside the lazy column.

### `contentPadding`

Supported platforms: Android.

Optional • Type: [ContentPadding](#contentpadding)

Content padding in dp.

### `horizontalAlignment`

Supported platforms: Android.

Optional • Literal type: `string`

The horizontal alignment of items.

Acceptable values are: `'start'` | `'end'` | `'center'`

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `verticalArrangement`

Supported platforms: Android.

Optional • Literal type: `union`

The vertical arrangement of items. Can be a preset string or an object with `spacedBy` to specify spacing in dp.

Acceptable values are: `'center'` | `'spaceBetween'` | `'spaceAround'` | `'spaceEvenly'` | `'top'` | `'bottom'` | `{ spacedBy: number }`

## Types

### `ContentPadding`

Supported platforms: Android.

Content padding values for LazyColumn.

| Property | Type | Description |
| --- | --- | --- |
| bottom(optional) | `number` | Bottom padding in dp. |
| end(optional) | `number` | End padding in dp. |
| start(optional) | `number` | Start padding in dp. |
| top(optional) | `number` | Top padding in dp. |
