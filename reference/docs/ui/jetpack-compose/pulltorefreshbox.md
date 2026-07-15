---
title: "PullToRefreshBox"
description: "A Jetpack Compose PullToRefreshBox component for pull-to-refresh interactions."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/pulltorefreshbox.md"
scraped_at: "2026-07-15T09:00:28.899026"
---

---
title: PullToRefreshBox
description: A Jetpack Compose PullToRefreshBox component for pull-to-refresh interactions.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# PullToRefreshBox

A Jetpack Compose PullToRefreshBox component for pull-to-refresh interactions.
Android, Included in Expo Go

> For a cross-platform list with pull-to-refresh, see [`List`](/versions/latest/sdk/ui/universal/list.md) — built on top of `PullToRefreshBox` on Android.

Expo UI PullToRefreshBox matches the official Jetpack Compose [PullToRefreshBox](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/package-summary#PullToRefreshBox\(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.pulltorefresh.PullToRefreshState,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1\)) API. It wraps scrollable content and shows a refresh indicator when pulled.

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

### Basic pull to refresh

Wrap scrollable content in a `PullToRefreshBox` to add pull-to-refresh behavior.

```tsx
import { useState, useCallback } from 'react';
import { Host, PullToRefreshBox, LazyColumn, ListItem } from '@expo/ui/jetpack-compose';

export default function BasicPullToRefresh() {
  const [refreshing, setRefreshing] = useState(false);

  const onRefresh = useCallback(() => {
    setRefreshing(true);
    setTimeout(() => {
      setRefreshing(false);
    }, 2000);
  }, []);

  return (
    <Host style={{ height: 400 }}>
      <PullToRefreshBox isRefreshing={refreshing} onRefresh={onRefresh}>
        <LazyColumn>
          <ListItem>
            <ListItem.HeadlineContent>Item 1</ListItem.HeadlineContent>
          </ListItem>
          <ListItem>
            <ListItem.HeadlineContent>Item 2</ListItem.HeadlineContent>
          </ListItem>
          <ListItem>
            <ListItem.HeadlineContent>Item 3</ListItem.HeadlineContent>
          </ListItem>
          <ListItem>
            <ListItem.HeadlineContent>Item 4</ListItem.HeadlineContent>
          </ListItem>
          <ListItem>
            <ListItem.HeadlineContent>Item 5</ListItem.HeadlineContent>
          </ListItem>
        </LazyColumn>
      </PullToRefreshBox>
    </Host>
  );
}
```

### Custom indicator colors

Use the `indicator` prop to customize the spinner and container colors.

```tsx
import { useState, useCallback } from 'react';
import { Host, PullToRefreshBox, LazyColumn, ListItem } from '@expo/ui/jetpack-compose';

export default function CustomIndicatorColors() {
  const [refreshing, setRefreshing] = useState(false);

  const onRefresh = useCallback(() => {
    setRefreshing(true);
    setTimeout(() => {
      setRefreshing(false);
    }, 2000);
  }, []);

  return (
    <Host style={{ height: 400 }}>
      <PullToRefreshBox
        isRefreshing={refreshing}
        onRefresh={onRefresh}
        indicator={{ color: '#6200EE', containerColor: '#F5F5F5' }}>
        <LazyColumn>
          <ListItem>
            <ListItem.HeadlineContent>Item 1</ListItem.HeadlineContent>
          </ListItem>
          <ListItem>
            <ListItem.HeadlineContent>Item 2</ListItem.HeadlineContent>
          </ListItem>
          <ListItem>
            <ListItem.HeadlineContent>Item 3</ListItem.HeadlineContent>
          </ListItem>
        </LazyColumn>
      </PullToRefreshBox>
    </Host>
  );
}
```

## API

```tsx
import { PullToRefreshBox } from '@expo/ui/jetpack-compose';
```

## Component

### `PullToRefreshBox`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[PullToRefreshBoxProps](#pulltorefreshboxprops)\>

A pull-to-refresh container that wraps scrollable content and shows a refresh indicator when pulled, matching Compose's `PullToRefreshBox`.

PullToRefreshBoxProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The content to refresh.

### `contentAlignment`

Supported platforms: Android.

Optional • Type: `ContentAlignment` • Default: `'topStart'`

Alignment of children within the box.

### `indicator`

Supported platforms: Android.

Optional • Type: [PullToRefreshIndicatorProps](#pulltorefreshindicatorprops)

Configuration for the loading indicator shown during pull-to-refresh.

### `isRefreshing`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Whether the content is refreshing.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onRefresh`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the user pulls to refresh.
