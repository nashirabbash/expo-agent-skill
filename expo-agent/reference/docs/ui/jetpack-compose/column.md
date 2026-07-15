---
title: "Column"
description: "A Jetpack Compose Column component for placing children vertically."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/column.md"
scraped_at: "2026-07-15T09:00:44.731890"
---

---
title: Column
description: A Jetpack Compose Column component for placing children vertically.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Column

A Jetpack Compose Column component for placing children vertically.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Column`](/versions/latest/sdk/ui/universal/column.md) — it renders the appropriate native component per platform.

Expo UI Column matches the official Jetpack Compose [Column](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Column) API and places children vertically with configurable arrangement and alignment.

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

`Column` places children vertically. Use `verticalArrangement` and `horizontalAlignment` to control spacing and alignment.

```tsx
import { Host, Column, Text } from '@expo/ui/jetpack-compose';
import { fillMaxWidth, paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function ColumnExample() {
  return (
    <Host matchContents>
      <Column
        verticalArrangement={{ spacedBy: 8 }}
        horizontalAlignment="center"
        modifiers={[fillMaxWidth(), paddingAll(16)]}>
        <Text>First</Text>
        <Text>Second</Text>
        <Text>Third</Text>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Column } from '@expo/ui/jetpack-compose';
```

## Component

### `Column`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ColumnProps](#columnprops)\>

ColumnProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `horizontalAlignment`

Supported platforms: Android.

Optional • Type: `HorizontalAlignment`

Horizontal alignment of children.

### `horizontalArrangement`

Supported platforms: Android.

Optional • Type: `HorizontalArrangement`

Horizontal arrangement of children.

### `verticalAlignment`

Supported platforms: Android.

Optional • Type: `VerticalAlignment`

Vertical alignment of children.

### `verticalArrangement`

Supported platforms: Android.

Optional • Type: `VerticalArrangement`

Vertical arrangement of children.

#### Inherited Props

-   `PrimitiveBaseProps`
