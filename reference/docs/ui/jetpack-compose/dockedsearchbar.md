---
title: "DockedSearchBar"
description: "A Jetpack Compose DockedSearchBar component for displaying an inline search input."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/dockedsearchbar.md"
scraped_at: "2026-07-15T09:00:30.386639"
---

---
title: DockedSearchBar
description: A Jetpack Compose DockedSearchBar component for displaying an inline search input.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# DockedSearchBar

A Jetpack Compose DockedSearchBar component for displaying an inline search input.
Android, Included in Expo Go

Expo UI DockedSearchBar matches the official Jetpack Compose [SearchBar API](https://developer.android.com/develop/ui/compose/components/search-bar) and displays a search input that remains anchored in its parent layout rather than expanding to full screen.

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

### Basic docked search bar

```tsx
import { useState } from 'react';
import { Host, DockedSearchBar } from '@expo/ui/jetpack-compose';

export default function BasicDockedSearchBarExample() {
  const [query, setQuery] = useState('');

  return (
    <Host matchContents>
      <DockedSearchBar onQueryChange={setQuery} />
    </Host>
  );
}
```

### With placeholder and leading icon

Use the `DockedSearchBar.Placeholder` and `DockedSearchBar.LeadingIcon` slot components to customize the search bar appearance.

```tsx
import { useState } from 'react';
import { Host, DockedSearchBar, Text } from '@expo/ui/jetpack-compose';

export default function DockedSearchBarWithSlotsExample() {
  const [query, setQuery] = useState('');

  return (
    <Host matchContents>
      <DockedSearchBar onQueryChange={setQuery}>
        <DockedSearchBar.Placeholder>
          <Text>Search items...</Text>
        </DockedSearchBar.Placeholder>
        <DockedSearchBar.LeadingIcon>
          <Text>🔍</Text>
        </DockedSearchBar.LeadingIcon>
      </DockedSearchBar>
    </Host>
  );
}
```

## API

```tsx
import { DockedSearchBar } from '@expo/ui/jetpack-compose';
```

## Components

### `DockedSearchBar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DockedSearchBarProps](#dockedsearchbarprops)\>

DockedSearchBarProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the component.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onQueryChange`

Supported platforms: Android.

Optional • Type: `(query: string) => void`

Callback function that is called when the search query changes.

### `DockedSearchBarLeadingIcon`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<LeadingIconProps\>

### `DockedSearchBarPlaceholder`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<PlaceholderProps\>
