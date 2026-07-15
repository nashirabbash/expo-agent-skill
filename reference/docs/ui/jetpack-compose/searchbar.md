---
title: "SearchBar"
description: "A Jetpack Compose SearchBar component for search input functionality."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/searchbar.md"
scraped_at: "2026-07-15T09:00:47.420978"
---

---
title: SearchBar
description: A Jetpack Compose SearchBar component for search input functionality.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# SearchBar

A Jetpack Compose SearchBar component for search input functionality.
Android, Included in Expo Go

Expo UI SearchBar matches the official Jetpack Compose [Search](https://developer.android.com/develop/ui/compose/components/search-bar) API and provides a search input with support for placeholder text and expanded full-screen search.

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

### Basic search bar

```tsx
import { useState } from 'react';
import { Host, SearchBar } from '@expo/ui/jetpack-compose';

export default function BasicSearchBarExample() {
  const [query, setQuery] = useState('');

  return (
    <Host matchContents>
      <SearchBar onSearch={searchText => setQuery(searchText)} />
    </Host>
  );
}
```

### Search bar with placeholder

Use the `SearchBar.Placeholder` sub-component to display hint text when the search field is empty.

```tsx
import { useState } from 'react';
import { Host, SearchBar } from '@expo/ui/jetpack-compose';

export default function SearchBarPlaceholderExample() {
  const [query, setQuery] = useState('');

  return (
    <Host matchContents>
      <SearchBar onSearch={searchText => setQuery(searchText)}>
        <SearchBar.Placeholder>Search items...</SearchBar.Placeholder>
      </SearchBar>
    </Host>
  );
}
```

## API

```tsx
import { SearchBar } from '@expo/ui/jetpack-compose';
```

## Components

### `ExpandedFullScreenSearchBar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ExpandedFullScreenSearchBarProps\>

ExpandedFullScreenSearchBar component for SearchBar. This component marks its children to be rendered in the expanded full-screen search bar.

### `SearchBar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<SearchBarProps\>

Renders a `SearchBar` component.

SearchBarProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the component.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onSearch`

Supported platforms: Android.

Optional • Type: `(searchText: string) => void`

Callback function that is called when the search text is submitted.

### `SearchBarPlaceholder`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<PlaceholderProps\>

Placeholder component for SearchBar. This component marks its children to be rendered in the placeholder slot.
