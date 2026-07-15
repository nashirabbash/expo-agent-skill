---
title: "Snackbar"
description: "A brief notification that appears at the bottom of the screen to provide feedback without interrupting the user."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/snackbar.md"
scraped_at: "2026-07-15T09:00:39.167776"
---

---
title: Snackbar
description: A brief notification that appears at the bottom of the screen to provide feedback without interrupting the user.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Snackbar

A brief notification that appears at the bottom of the screen to provide feedback without interrupting the user.
Android, Included in Expo Go

Expo UI exposes two components that mirror Jetpack Compose's [Snackbar](https://developer.android.com/develop/ui/compose/components/snackbar) APIs:

-   [`SnackbarHost`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbarhost) wraps Compose's [SnackbarHost](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarHost.composable) and [SnackbarHostState](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarHostState). Place it once in your layout, then call `showSnackbar` on the `ref`. Snackbars auto-dismiss based on `duration` and can also be dismissed via the action button or the optional close icon.
-   [`Snackbar`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbar) is a styling-only child of [`SnackbarHost`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbarhost). Pass one to override colors or place the action on a new line.

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

### Showing a snackbar

Place a [`SnackbarHost`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbarhost) once in your layout and call `showSnackbar` on its ref to display a message. The returned promise resolves with `'actionPerformed'` or `'dismissed'` once the snackbar goes away.

```tsx
import { useRef } from 'react';
import {
  Box,
  Button,
  Column,
  Host,
  SnackbarHost,
  Text,
  type SnackbarHostRef,
} from '@expo/ui/jetpack-compose';
import { align, fillMaxSize, fillMaxWidth, padding } from '@expo/ui/jetpack-compose/modifiers';

export default function SnackbarExample() {
  const hostRef = useRef<SnackbarHostRef>(null);

  const onArchive = async () => {
    const result = await hostRef.current?.showSnackbar({
      message: 'Item archived',
      actionLabel: 'Undo',
      duration: 'short',
    });
    if (result === 'actionPerformed') {
      // The user tapped Undo, restore the item.
    }
  };

  return (
    <Host style={{ flex: 1 }}>
      <Box modifiers={[fillMaxSize()]}>
        <Column modifiers={[padding(16, 16, 16, 16)]}>
          <Button onClick={onArchive}>
            <Text>Archive</Text>
          </Button>
        </Column>

        <Box modifiers={[align('bottomCenter'), fillMaxWidth()]}>
          <SnackbarHost ref={hostRef} />
        </Box>
      </Box>
    </Host>
  );
}
```

### Custom styling

Pass a [`Snackbar`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbar) child to [`SnackbarHost`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbarhost) to override colors or place the action on a new line. The [`Snackbar`](/versions/latest/sdk/ui/jetpack-compose/snackbar.md#snackbar) itself takes no content, the message and action come from each `showSnackbar` call.

```tsx
import { useRef } from 'react';
import {
  Box,
  Button,
  Column,
  Host,
  Snackbar,
  SnackbarHost,
  Text,
  type SnackbarHostRef,
} from '@expo/ui/jetpack-compose';
import { align, fillMaxSize, fillMaxWidth, padding } from '@expo/ui/jetpack-compose/modifiers';

export default function StyledSnackbar() {
  const hostRef = useRef<SnackbarHostRef>(null);

  const onSave = () => {
    hostRef.current?.showSnackbar({
      message: 'Saved',
      actionLabel: 'Undo',
    });
  };

  return (
    <Host style={{ flex: 1 }}>
      <Box modifiers={[fillMaxSize()]}>
        <Column modifiers={[padding(16, 16, 16, 16)]}>
          <Button onClick={onSave}>
            <Text>Save</Text>
          </Button>
        </Column>

        <Box modifiers={[align('bottomCenter'), fillMaxWidth()]}>
          <SnackbarHost ref={hostRef}>
            <Snackbar
              containerColor="#1E1E2E"
              contentColor="#CDD6F4"
              actionContentColor="#F38BA8"
              dismissActionContentColor="#CDD6F4"
            />
          </SnackbarHost>
        </Box>
      </Box>
    </Host>
  );
}
```

## API

```tsx
import { Snackbar, SnackbarHost } from '@expo/ui/jetpack-compose';
```

## Components

### `Snackbar`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SnackbarProps](#snackbarprops)\>

Styling configuration for the snackbar shown by `SnackbarHost`. Pass as a child to override colors or place the action on a new line.

SnackbarProps

### `actionContentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The content color used for the action button.

### `actionOnNewLine`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Whether the action should be placed on a new line below the message. Useful for long action labels.

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The background color of the snackbar container.

### `contentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The preferred content color used for the message text.

### `dismissActionContentColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

The content color used for the dismiss-action icon button.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `SnackbarHost`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SnackbarHostProps](#snackbarhostprops)\>

A Material 3 [SnackbarHost](https://developer.android.com/develop/ui/compose/components/snackbar) that displays snackbars triggered via its ref's `showSnackbar` method.

SnackbarHostProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Optional `Snackbar` child supplying styling for shown snackbars. Mirrors Compose's `SnackbarHost(hostState) { data -> Snackbar(data, ...) }` lambda.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `ref`

Supported platforms: Android.

Optional • Type: Ref<[SnackbarHostRef](#snackbarhostref)\>

Ref exposing the imperative `showSnackbar` method.

## Types

### `SnackbarDuration`

Supported platforms: Android.

Literal Type: `string`

How long the snackbar is shown. Mirrors Compose's `SnackbarDuration` enum.

Acceptable values are: `'short'` | `'long'` | `'indefinite'`

### `SnackbarHostRef`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| showSnackbar | (options: [SnackbarShowOptions](#snackbarshowoptions)) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[SnackbarResult](#snackbarresult)\> | Shows a snackbar and resolves with `'actionPerformed'` when the user taps the action, or `'dismissed'` when it times out or the dismiss-action button is tapped. Subsequent calls queue and show after the current snackbar is dismissed. |

### `SnackbarResult`

Supported platforms: Android.

Literal Type: `string`

Reason a snackbar invocation resolved. Mirrors Compose's `SnackbarResult` enum.

Acceptable values are: `'actionPerformed'` | `'dismissed'`

### `SnackbarShowOptions`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| actionLabel(optional) | `string` | Label for the optional action button. When omitted, no action button is shown. |
| duration(optional) | [SnackbarDuration](#snackbarduration) | How long to show the snackbar. Defaults to `'short'` when an `actionLabel` is not provided, and `'indefinite'` when it is, matching Compose. |
| message | `string` | The message body of the snackbar. |
| withDismissAction(optional) | `boolean` | Whether to show a trailing close (X) icon button to dismiss the snackbar. Default: `false` |
